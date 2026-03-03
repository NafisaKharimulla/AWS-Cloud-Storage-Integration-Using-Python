import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

BUCKET_NAME = "nafisa-s3-project-2026"

def upload_file(file_path):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found.")

        s3 = boto3.client("s3")
        file_name = os.path.basename(file_path)

        print(f"Uploading {file_name} to S3...")
        s3.upload_file(file_path, BUCKET_NAME, file_name)

        print(" Upload successful.")

    except FileNotFoundError as e:
        print("Filenoterror", e)

    except NoCredentialsError:
        print(" AWS credentials not configured.")

    except PartialCredentialsError:
        print(" Incomplete AWS credentials.")

    except ClientError as e:
        print(" AWS Error:", e)


if __name__ == "__main__":
    path = input("Enter file name to upload: ")
    upload_file(path)
