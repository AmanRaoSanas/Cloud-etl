# Cloud Data Pipelines 🚀

This repository contains scalable, cloud-native data pipelines built using AWS services, Python, Airflow, and Terraform.

## 🧩 What’s Inside

### 🛠️ ETL Jobs
- **glue_job1_sales_data.py** – AWS Glue ETL job for processing sales data from S3 to Redshift
- **lambda_transformer.py** – AWS Lambda function to clean & enrich real-time events
- **airflow_dag_example.py** – Airflow DAG that orchestrates a multi-step ETL workflow

### ☁️ CloudFormation IaC
Reusable CloudFormation templates to provision:
- AWS Glue Job + IAM Role
- S3 Bucket for input/output
- (Coming Soon) Redshift, Step Functions, CloudWatch alerts


### 📒 Jupyter Notebooks
- Data exploration and schema inspection using Pandas & Spark

### 📌 Architecture Diagram
- Visual representation of pipeline components and data flow  
  ![pipeline](assets/pipeline_architecture.png)

---

## 📚 Tech Stack
- **Languages**: Python, SQL
- **Cloud**: AWS (Glue, Lambda, S3, Redshift, CloudWatch)
- **Orchestration**: Airflow, Step Functions
- **IaC**: Terraform
- **Monitoring**: CloudWatch Logs & Alerts

---

## 🧠 Use Cases
- Real-time event processing
- Batch ETL pipeline orchestration
- Infrastructure automation
- Data quality monitoring

---

## 🔗 Author
**Aman Rao Sanas**  
[LinkedIn](https://linkedin.com/in/amanraosanas) | [Portfolio](https://amanraosanas.github.io/portfolio) | [Email](mailto:amanraosanas17@gmail.com)
