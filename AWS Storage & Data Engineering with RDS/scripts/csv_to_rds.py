import pandas as pd
import pyodbc

df = pd.read_csv("cleaned_ecommerce_data.csv")

conn = pyodbc.connect(
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com,1433;"
"DATABASE=ecommerce;"
"UID=admin;"
"PWD=nafisashaik"
)

cursor = conn.cursor()
cursor.fast_executemany = True

data = list(df[['InvoiceNo','Description','Country','UnitPrice','Quantity','InvoiceDate']].itertuples(index=False, name=None))

batch_size = 500

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]

    cursor.executemany(
    "INSERT INTO sales_data (order_id, product_name, category, price, quantity, order_date) VALUES (?,?,?,?,?,?)",
    batch
    )

    conn.commit()
    print("Inserted rows:", i + len(batch))

cursor.close()
conn.close()

print("CSV import completed successfully")
