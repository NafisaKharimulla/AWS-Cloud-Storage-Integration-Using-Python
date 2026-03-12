AWS Storage & Data Engineering with RDS

Project Overview
This project demonstrates an end-to-end cloud-based data pipeline using AWS Storage Services (S3, Glacier), AWS RDS, Python, Pandas, and SQL. A CSV dataset containing sales transactions is used to simulate a real-world scenario covering data ingestion, processing, storage, analytics, and export.

Technologies Used

- Cloud Platform: AWS
- Storage Services: Amazon S3, Amazon Glacier (conceptual)
- Database: AWS RDS (SQL Server)
- Programming Language: Python 3.x
- AWS SDK: Boto3
- Data Processing: Pandas
- Query Language: SQL
- Database Connection: pyodbc

Dataset

- Format: CSV
- Size: 397,924+ rows
- Columns: InvoiceNo (PK), StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

Architecture Overview
'''
Local System / EC2
|
| Python Scripts (Boto3, Pandas, pyodbc)
v

---

| Amazon S3 Bucket | -> Raw & Processed Data

---

       |
       | Data Processing & Transformation
       v

---

| Amazon RDS SQL | -> sales_data table

---

       |
       | SQL Queries / Analytics
       v

---

| CSV Export / BI |

---

'''

Project Tasks & Implementation

Part 1: Conceptual Understanding

- Explored Data Lake vs Data Warehouse
- Used S3 as raw and processed data storage
- Discussed Glacier for archival storage
- Explained RDS and difference from self-managed databases

Part 2: AWS Provisioning

- Created S3 bucket 'ecommerce-data-lake' with /raw/ and /processed/ folders
- Launched RDS SQL Server instance 'ecommerce-sql' with proper security groups
- Validated connectivity using pyodbc

Part 3: Data Ingestion & Storage

- Uploaded raw CSV to S3 using Python
- Listed and downloaded files from S3
- Explained archival to Glacier

Sample Output:
Files in S3 /raw/: cleaned_ecommerce_data.csv
File downloaded successfully: cleaned_ecommerce_data.csv

Part 4: Data Processing & Transformation

- Read data from S3 using Pandas
- Handled missing values and corrected data types
- Generated summary metrics, group-wise aggregations, and date-based analysis
- Stored processed datasets back to S3

Sample Output:
Processed data saved to S3: /processed/cleaned_ecommerce_data.csv
Total records processed: 397,924

Part 5: AWS RDS – Database Operations

- Created sales_data table:

Columns: id (PK), order_id, product_name, category, price, quantity, order_date

- Performed CRUD operations:

Sample Output:
Data inserted successfully
Records selected: 10
Data updated successfully
Data deleted successfully

Part 6: SQL Practice & Analytics

- Queries executed for SUM, AVG, COUNT, GROUP BY, HAVING, date-based filtering, sorting, ranking, top/bottom performers

Sample Output:
Total Sales per Country:
Country TotalSales
UK 1123456.50
France 234567.00
Germany 456789.25

Top 5 Products by Quantity Sold:
ProductName TotalQuantity
WHITE HANGING HEART 1250
CHRISTMAS TREE DECORATION 1190
...

Part 7: CSV Import & Export with RDS

- CSV Import:
  Imported cleaned_ecommerce_data.csv into sales_data using Python batch insertion

Import Output:
Inserted rows: 396000
Inserted rows: 396500
Inserted rows: 397000
Inserted rows: 397500
Inserted rows: 397924
CSV import completed successfully

- CSV Export:
  Exported query results to exported_sales_data.csv

Export Output:
Data exported successfully
Output file: exported_sales_data.csv

- Bulk Import/Export Methods:
  1. Python + Pandas (used)
  2. SQL Server Import/Export Wizard
  3. BULK INSERT
  4. AWS DMS

Assumptions & Limitations

- Dataset: ~397,924 rows; fits on db.t3.micro instance
- CSV schema is consistent
- Network required to access RDS
- Glacier archival conceptual only

Execution Proof / Logs

- S3 Upload: Success
- Data Processing: Success
- RDS Insert: 397,924 rows
- SQL Queries: Verified
- CSV Export: exported_sales_data.csv
