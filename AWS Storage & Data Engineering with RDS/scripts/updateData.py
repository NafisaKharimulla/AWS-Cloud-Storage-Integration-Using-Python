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
UPDATE sales_data
SET price = 900
WHERE order_id = 1
""")

conn.commit()

print("Data updated successfully")

cursor.close()
conn.close()
