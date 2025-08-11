import boto3
import io
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    raw_bucket = 'pass_none'
    clean_bucket = 'pass_none'

    try:
        key = event['Records'][0]['s3']['object']['key']
        logging.info(f"Trigger for the file: {key}")

        obj = s3.get_object(Bucket = raw_bucket, Key = key)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        logging.info(f"Read CSV file from S3: {key}")

        if 'Date' not in df.columns:
            raise ValueError("Date column missing in CSV")

        df = df.dropna()

        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

        df = df.sort_values(by='Date', ascending= True)
        df['Sale_ID'] = ["fS{i:03}" for i in range(1, len(df)+1)]

        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)

        clean_Key = f"cleaned_{key}"
        s3.put_object(Bucket = clean_bucket, Key = clean_Key, Body = csv_buffer.getvalue())
        logging.info(f"Cleaned data uploaded to S3: {clean_Key}")

        return{
            'statusCode': 200,
            'body': f'ETL completed for file: {key}'
        }

    except Exception as e:
        logging.error(f"ETL failed due to: {str(e)}")
        return {
            'statuscode': 500,
            'body': f"ETL failed due to: {str(e)}"
        }



