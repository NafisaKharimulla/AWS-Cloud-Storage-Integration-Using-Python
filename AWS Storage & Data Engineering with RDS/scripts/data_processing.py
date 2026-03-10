import boto3
import pandas as pd
from io import BytesIO

# ------------------------------
# Step 1: Read data from S3
# ------------------------------
s3 = boto3.client('s3')
bucket_name = "nafisa-s3-project-2026"
raw_key = "raw/cleaned_ecommerce_data.csv"

obj = s3.get_object(Bucket=bucket_name, Key=raw_key)
df = pd.read_csv(obj['Body'])
print("Raw data loaded from S3")
print(df.head())

# ------------------------------
# Step 2: Basic cleaning
# ------------------------------
# Check missing values
print("Missing values per column:")
print(df.isnull().sum())

# Fill missing numeric columns with mean
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Correct data types if necessary
# Example: df['date_column'] = pd.to_datetime(df['date_column'])

print("Data cleaned successfully")

# ------------------------------
# Step 3: Generate summary metrics
# ------------------------------
print("Summary metrics:")
print(df.describe())

# Example group-wise aggregation
# Step-4:
# Replace 'category_column' with an actual column name in your dataset
if 'category_column' in df.columns:
    group_summary = df.groupby('category_column').mean()
    print("Group-wise aggregation:")
    print(group_summary)



# ------------------------------
# Step 5: Additional Transformations
# ------------------------------

# Example: Create TotalRevenue column if quantity and price exist
if 'quantity' in df.columns and 'price' in df.columns:
    df['TotalRevenue'] = df['quantity'] * df['price']
    print("Added TotalRevenue column")

# ------------------------------
# Step 6: Group-wise Aggregation
# ------------------------------
if 'category_column' in df.columns and 'TotalRevenue' in df.columns:
    group_summary = df.groupby('category_column').agg({'TotalRevenue': 'sum'})
    print("Group-wise aggregation (TotalRevenue per category):")
    print(group_summary)

# ------------------------------
# Step 7: Date-based Aggregation
# ------------------------------
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Monthly aggregation
    monthly_summary = df.groupby(df['order_date'].dt.to_period('M')).agg({'TotalRevenue': 'sum'})
    print("Monthly TotalRevenue:")
    print(monthly_summary)

    # Weekly aggregation (optional)
    weekly_summary = df.groupby(df['order_date'].dt.to_period('W')).agg({'TotalRevenue': 'sum'})
    print("Weekly TotalRevenue:")
    print(weekly_summary)

# ------------------------------
# Step 8: Store fully processed data back to S3
# ------------------------------
processed_key = "processed/processed_data.csv"
csv_buffer = BytesIO()
df.to_csv(csv_buffer, index=False)
s3.put_object(Bucket=bucket_name, Key=processed_key, Body=csv_buffer.getvalue())
print(f"Processed data uploaded to s3://{bucket_name}/{processed_key}")

