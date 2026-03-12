import pyodbc

conn = pyodbc.connect(
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com,1433;"
"DATABASE=ecommerce;"
"UID=admin;"
"PWD=nafisashaik"
)

cursor = conn.cursor()

cursor.execute("""
SELECT TOP 5 product_name,
SUM(quantity) AS total_sales
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
