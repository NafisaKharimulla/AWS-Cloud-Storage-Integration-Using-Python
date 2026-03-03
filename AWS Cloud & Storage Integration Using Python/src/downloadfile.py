import boto3
import os
import hashlib
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

# ==========================================================
# CONFIGURATION
# ==========================================================

BUCKET_NAME = "nafisa-s3-project-2026"

# ==========================================================
# FUNCTION 1: LIST FILES IN BUCKET
# ==========================================================

def list_files():
    try:
        s3 = boto3.client("s3")

        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        print("\n===== FILES IN S3 BUCKET =====")

        if "Contents" in response:
            for obj in response["Contents"]:
                print(f"- {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("No files found.")

    except ClientError as e:
        print("AWS Error:", e)


# ==========================================================
# FUNCTION 2: DOWNLOAD FILE FROM S3
# ==========================================================

def download_file(object_name):
    try:
        s3 = boto3.client("s3")

        local_file = "downloaded_" + os.path.basename(object_name)

        print(f"\nDownloading {object_name}...")
        s3.download_file(BUCKET_NAME, object_name, local_file)

        print("Download successful.")
        return local_file

    except FileNotFoundError:
        print("Local path error.")

    except NoCredentialsError:
        print("AWS credentials not configured.")

    except PartialCredentialsError:
        print("Incomplete AWS credentials.")

    except ClientError as e:
        print("AWS Error:", e)


# ==========================================================
# FUNCTION 3: VERIFY FILE INTEGRITY (MD5 CHECK)
# ==========================================================

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def verify_integrity(original_file, downloaded_file):
    print("\n===== VERIFYING FILE INTEGRITY =====")

    md5_original = calculate_md5(original_file)
    md5_downloaded = calculate_md5(downloaded_file)

    print("Original File MD5  :", md5_original)
    print("Downloaded File MD5:", md5_downloaded)

    if md5_original == md5_downloaded:
        print(" Files are identical.")
    else:
        print("Files are different.")


# ==========================================================
# MAIN PROGRAM (Sequential Execution)
# ==========================================================

if __name__ == "__main__":

    # Step 1: List files
    list_files()

    # Step 2: Ask which file to download
    object_key = input("\nEnter S3 file name to download: ")

    # Step 3: Download file
    downloaded_file = download_file(object_key)

    # Step 4: Verify integrity (compare with original local file)
    if downloaded_file:
        original_file = input("Enter original local file name to compare: ")
        verify_integrity(original_file, downloaded_file)
