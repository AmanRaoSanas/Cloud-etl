You are an expert AWS Data Engineer.

I have a project called `aws-etl-pipeline` which builds a serverless, CI/CD-based ETL pipeline using AWS services like S3, Lambda, CloudFormation, and GitHub Actions.

💡 Use Case:
CSV files are uploaded to a raw-data S3 bucket, a Lambda function (Python + Pandas) cleans/transforms the data, and stores cleaned output into another S3 bucket. The whole infra is deployed via CloudFormation, and CI/CD is done using GitHub Actions.

🧱 Project Structure:

aws-etl-pipeline/
├── etl_jobs/
│   ├── lambda_etl.py           # Contains ETL logic, works for both AWS & local
│   ├── requirements.txt        # Contains: pandas
├── cloudformation/
│   └── template.yaml           # Deploys raw + clean S3 buckets, Lambda, trigger, IAM role
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions pipeline to deploy ZIP and stack
├── data/
│   └── raw/sales_data.csv
│   └── processed/cleaned_sales_data.csv
├── README.md
├── .gitignore                  # Should ignore /lambda/package/ and lambda-deploy.zip
├── lambda-deploy.zip  

📦 lambda/lambda_etl.py contains dual-mode logic:
- When deployed to AWS, it uses boto3 to read raw CSV from S3 → clean → write to another S3 bucket
- When run locally, it reads `data/raw/sample_input.csv`, transforms, and writes to `data/processed/`

✅ Goals:
- Enable local testing via `python lambda/lambda_etl.py`
- Enable full cloud deployment using GitHub Actions (CI/CD)
- Clean, production-grade project
- Athena and Glue integration can be added later

🔐 I use AWS CLI locally, so if S3 boto3 access is needed, I run `aws configure` to set credentials.

🎯 Help me continue working on this project from wherever we left off. If I say "continue", assume I'm referring to this project.
