import boto3

s3 = boto3.client("s3")

bucket = "nafisa-s3-project-2026"

response = s3.list_objects_v2(Bucket=bucket)

for obj in response.get("Contents", []):
    print(obj["Key"])
