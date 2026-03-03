import boto3
import os
import hashlib
import logging
from botocore.exceptions import ClientError

# ==========================================================
# LOGGING SETUP
# ==========================================================

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==========================================================
# CREATE S3 CLIENT
# ==========================================================

def create_s3_client(region):
    return boto3.client("s3", region_name=region)


# ==========================================================
# LIST FILES
# ==========================================================

def list_files(s3, bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        print("\n=== Files in Bucket ===")
        if "Contents" in response:
            for obj in response["Contents"]:
                print(f"{obj['Key']}  ({obj['Size']} bytes)")
        else:
            print("Bucket is empty.")

    except ClientError as e:
        logging.error(e)


# ==========================================================
# UPLOAD FILE
# ==========================================================

def upload_file(s3, bucket_name, file_path):
    try:
        if not os.path.isfile(file_path):
            logging.error("Upload failed: File not found.")
            return None

        file_name = os.path.basename(file_path)

        s3.upload_file(file_path, bucket_name, file_name)
        logging.info("File uploaded successfully.")
        return file_name

    except ClientError as e:
        logging.error(e)
        return None


# ==========================================================
# DOWNLOAD FILE
# ==========================================================

def download_file(s3, bucket_name, object_key):
    try:
        download_path = "downloaded_" + object_key

        s3.download_file(bucket_name, object_key, download_path)
        logging.info("File downloaded successfully.")

        return download_path

    except ClientError as e:
        logging.error(e)
        return None


# ==========================================================
# MD5 CHECKSUM
# ==========================================================

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def verify_integrity(original_file, downloaded_file):
    if not original_file or not downloaded_file:
        logging.warning("Integrity check skipped.")
        return

    md5_original = calculate_md5(original_file)
    md5_downloaded = calculate_md5(downloaded_file)

    print("\n=== File Integrity Check ===")
    print("Original MD5   :", md5_original)
    print("Downloaded MD5 :", md5_downloaded)

    if md5_original == md5_downloaded:
        logging.info("Integrity Verified: Files are identical.")
    else:
        logging.warning("Integrity Failed: Files differ.")


# ==========================================================
# MAIN EXECUTION (NO CHOICE)
# ==========================================================

def main():

    #  Parameter Inputs
    bucket_name = input("Enter S3 bucket name: ")
    region = input("Enter AWS region (example: ap-south-1): ")
    local_file_path = input("Enter local file path to upload: ")

    #  Create Client
    s3 = create_s3_client(region)

    # List existing files
    list_files(s3, bucket_name)

    # Upload file
    uploaded_file_name = upload_file(s3, bucket_name, local_file_path)

    # List again after upload
    list_files(s3, bucket_name)

    # Download uploaded file
    downloaded_file = download_file(s3, bucket_name, uploaded_file_name)

    # 5️⃣erify integrity
    verify_integrity(local_file_path, downloaded_file)


if __name__ == "__main__":
    main()
