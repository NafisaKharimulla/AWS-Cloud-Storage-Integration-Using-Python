import boto3

s3 = boto3.client("s3")

bucket = "nafisa-s3-project-2026"
key = "raw/cleaned_ecommerce_data.csv"

s3.download_file(bucket, key, "cleaned_ecommerce_data.csv")

print("File downloaded successfully")
