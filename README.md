# Serverless ETL Pipeline on AWS

This project implements a **serverless ETL pipeline** using **AWS Lambda, S3, CloudFormation, and GitHub Actions**.

## Tech Stack
- AWS Lambda (Python)
- AWS S3 (Raw & Cleaned buckets)
- AWS CloudFormation (IaC)
- GitHub Actions (CI/CD)
- Pandas (for data transformation)
- CloudWatch (Logging)

##  How It Works
1. Upload a CSV file to `etl-pipeline-raw-data-1`
2. Lambda gets triggered:
   - Drops nulls
   - Formats date
   - Adds `Sale_ID`
3. Cleaned file saved to `etl-pipeline-cleaned-data-1`

## Sample Input & Output
**Raw File:**
| Date       | Product | Quantity |
|------------|---------|----------|
| 2025-08-14 | Shirt   | 10       |

**Cleaned File:**
| Sale_ID | Date       | Product | Quantity |
|---------|------------|---------|----------|
| 1       | 14-08-2025 | Shirt   | 10       |

## Deployment
Use `cloudformation.yaml` to deploy resources. Lambda is auto-deployed via GitHub Actions.

## Future Improvements (Planned)
- Glue + Athena integration
- Email notification after ETL
- Data profiling summary

---

## Author
**Aman Rao Sanas**  
_Data Engineer | Python | AWS | Scalable Data Pipelines_  
