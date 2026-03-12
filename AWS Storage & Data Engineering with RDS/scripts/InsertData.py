import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com,1433;"
    "DATABASE=ecommerce;"
    "UID=admin;"
    "PWD=nafisashaik"
)

cursor = conn.cursor()

# insert data
cursor.execute("""
INSERT INTO sales_data
VALUES (1,'Laptop','Electronics',800,1,'2024-01-10')
""")

conn.commit()

print("Data inserted")
