import boto3
import pandas as pd
from io import BytesIO

# Initialize S3 client
s3 = boto3.client('s3')
bucket_name = "nafisa-s3-project-2026"
key = "raw/cleaned_ecommerce_data.csv"

# Download file object from S3
obj = s3.get_object(Bucket=bucket_name, Key=key)

# Load CSV into pandas
df = pd.read_csv(obj['Body'])
print("Data loaded from S3")
print(df.head())
