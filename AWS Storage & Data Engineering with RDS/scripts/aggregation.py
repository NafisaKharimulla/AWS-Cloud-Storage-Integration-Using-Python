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
SELECT 
COUNT(*) AS total_orders,
SUM(quantity) AS total_items_sold,
AVG(price) AS average_price
FROM sales_data
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
