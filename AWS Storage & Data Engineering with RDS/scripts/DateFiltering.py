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
SELECT *
FROM sales_data
WHERE order_date >= '2024-01-01'
AND order_date <= '2024-12-31'
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
