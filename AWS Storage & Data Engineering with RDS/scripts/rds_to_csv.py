import pandas as pd
import pyodbc

conn = pyodbc.connect(
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com,1433;"
"DATABASE=ecommerce;"
"UID=admin;"
"PWD=nafisashaik"
)

query = "SELECT TOP 1000 * FROM sales_data"

df = pd.read_sql(query, conn)

df.to_csv("exported_sales_data.csv", index=False)

print("Data exported successfully")

conn.close()
