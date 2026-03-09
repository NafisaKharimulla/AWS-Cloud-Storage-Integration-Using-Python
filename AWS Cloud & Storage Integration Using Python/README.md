# AWS Cloud & Storage Integration Using Python

## Objective

This project demonstrates how Python interacts with AWS cloud services to perform real-world data transfer tasks. The implementation uses the AWS SDK for Python (Boto3) to upload and download files from Amazon S3 while handling errors and automating the workflow.

The project also explores cloud computing concepts and explains how the same scripts can run on an EC2 instance.

---

# Part 1: Cloud & AWS Understanding

## What is Cloud Computing

Cloud computing is the delivery of computing services such as servers, storage, databases, networking, and software over the internet instead of maintaining physical infrastructure locally.

Benefits:

- Scalability
- Cost efficiency
- High availability
- Global accessibility

---

## Cloud Service Models

### IaaS (Infrastructure as a Service)

Provides virtualized computing resources such as servers, storage, and networking.

Example:

- Amazon EC2

### PaaS (Platform as a Service)

Provides a platform for developers to build and deploy applications without managing infrastructure.

Example:

- AWS Elastic Beanstalk

### SaaS (Software as a Service)

Provides software applications over the internet.

Examples:

- Gmail
- Google Docs

---

## Why AWS is Used

AWS provides reliable, scalable, and cost-effective cloud computing services used by organizations worldwide.

Common use cases:

- Web application hosting
- Data storage and backup
- Big data analytics
- Machine learning systems
- Disaster recovery

---

# AWS Services Used

## Amazon S3

:contentReference[oaicite:0]{index=0}  
Amazon S3 is used to store files in the cloud. The Python scripts upload files to the bucket, list bucket objects, and download files back to the local system.

Features:

- Highly durable storage
- Scalable
- Secure object storage

---

## Amazon EC2

:contentReference[oaicite:1]{index=1}  
Amazon EC2 provides virtual machines in the cloud where the same Python scripts can run instead of running locally.

---

## AWS IAM

:contentReference[oaicite:2]{index=2}  
IAM is used to securely manage permissions and credentials for accessing AWS resources.

---

# Part 2: AWS Setup & Exploration

Steps performed:

1. Created an AWS account
2. Configured IAM user with access keys
3. Configured AWS CLI using

aws configure

4. Launched an EC2 instance using Free Tier
5. Created an S3 bucket
6. Configured bucket permissions

Concepts learned:

- Regions and Availability Zones
- Public vs Private S3 access
- IAM roles and policies

---

# Part 3: Python + Boto3 Data Transfer

## Upload Script

Uploads files from the local system to the S3 bucket.

Features:

- Upload small CSV files
- Upload large files
- Error handling for:
  - File not found
  - Invalid credentials
  - Bucket not available

Run using:

python upload_to_s3.py

---

## Download Script

Downloads files from S3 to the local system.

Features:

- Retrieve objects from S3
- Save them locally
- Verify file integrity

Run using:

python downloadfile.py

---

## List Files Script

Lists all files inside the S3 bucket.

Run using:

python list_files.py

Example Output:

BooksDataset.csv  
large_stock_data.csv

---

# Part 4: Automation & Logic

An automation script was created to perform all tasks automatically.

Features:

- Parameterized bucket name
- Parameterized file paths
- Parameterized AWS region
- Modular Python functions
- Logging for execution tracking
- No hardcoded credentials

Workflow:

1. List files in the S3 bucket
2. Upload file to S3
3. Download the file from S3
4. Verify file integrity

Run using:

python s3_full_automation.py

---

# Error Handling

The scripts handle the following scenarios:

- File not found errors
- Invalid AWS credentials
- Bucket not available
- AWS API connection issues

---

# Part 5: EC2 Context

## Running Scripts on EC2

The same scripts can run on an EC2 instance.

Steps:

1. Launch EC2 instance
2. Install Python and Boto3
3. Transfer project files to EC2
4. Run:

python3 s3_full_automation.py

---

## Local vs EC2 Execution

Local System:

- Uses local computer resources
- Requires AWS CLI configuration

EC2 Instance:

- Runs in the cloud
- Can run continuously
- More scalable

---

## IAM Role Advantage

Instead of storing AWS access keys in code, IAM roles can be attached to EC2 instances.

Benefits:

- Increased security
- No credential storage
- Automatic credential rotation

---

# Project Structure

AWS-Cloud-Storage-Python/
│
├── Documents
│ ├── Contest.txt
│ ├── Setup Steps.txt
│
├── Screenshots
│ ├── EC2 running.png
│ ├── Instance Launched.png
│ ├── Upload the files.png
│
├── Scripts
│ ├── aws_setup.sh
│ ├── upload_to_s3.py
│ ├── downloadfile.py
│ ├── s3_full_automation.py
│
├── README.md

---

# Script Workflow

Local System  
↓  
Python + Boto3  
↓  
Amazon S3 Bucket  
↓  
Download  
↓  
Local System

---

# Assumptions

- AWS CLI is configured
- User has permissions to access S3
- Python and Boto3 are installed
- Internet connection is available

---

# Limitations

- Network speed affects large file transfers
- File integrity check uses checksum comparison
- Bucket permissions must be configured correctly

---

# Proof of Execution

The project includes:

- Terminal logs showing successful uploads and downloads
- Screenshots of EC2 instance running
- Screenshots of files stored in S3 bucket
- Downloaded files verified locally

---

# Conclusion

This project demonstrates how Python can integrate with AWS cloud services to automate data transfer workflows. It highlights practical use of S3 storage, EC2 cloud execution, and secure credential management using IAM.
