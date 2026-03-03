#!/bin/bash

# ============================================================

# PART 2: AWS SETUP & EXPLORATION - VERIFICATION SCRIPT

# ============================================================

# This script verifies:

# 1. AWS CLI installation

# 2. AWS CLI configuration

# 3. S3 bucket existence / creation

# 4. Key pair permission security

# ------------------------------------------------------------

# Step 1: Check if AWS CLI is installed

# ------------------------------------------------------------

if ! command -v aws &> /dev/null
then
echo "AWS CLI is not installed. Please install AWS CLI first."
exit 1
fi

echo "AWS CLI is installed."

# ------------------------------------------------------------

# Step 2: Verify AWS CLI Configuration

# ------------------------------------------------------------

echo "Checking AWS credentials..."

aws sts get-caller-identity > /dev/null 2>&1

if [ $? -ne 0 ]; then
echo "AWS CLI is not configured properly."
echo "Run: aws configure"
exit 1
fi

echo "AWS CLI is configured correctly."

# ------------------------------------------------------------

# Step 3: Create S3 Bucket (if it does not exist)

# ------------------------------------------------------------

BUCKET_NAME="nafisa-s3-project-2026"
REGION="ap-south-1"

echo "Checking if S3 bucket exists..."

aws s3api head-bucket --bucket $BUCKET_NAME > /dev/null 2>&1

if [ $? -eq 0 ]; then
echo "S3 bucket already exists."
else
echo "Creating S3 bucket..."
aws s3 mb s3://$BUCKET_NAME --region $REGION
fi

# ------------------------------------------------------------

# Step 4: List S3 Buckets

# ------------------------------------------------------------

echo "Listing S3 buckets:"
aws s3 ls

# ------------------------------------------------------------

# Step 5: Secure EC2 Key Pair Permissions

# ------------------------------------------------------------

KEY_FILE="nafisa-ec2-key.pem"

if [ -f "$KEY_FILE" ]; then
chmod 400 $KEY_FILE
echo "Key file permissions set to 400."
else
echo "Key file not found in current directory."
fi

# ------------------------------------------------------------

# Script Completed

# ------------------------------------------------------------

echo "Part 2 Setup Verification Completed Successfully."
