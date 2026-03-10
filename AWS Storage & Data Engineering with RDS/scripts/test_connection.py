import pyodbc

server = "ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com"
database = "ecommerce"
username = "admin"
password = "nafisashaik"

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server},1433;"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

print("Connected to ecommerce database")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE orders (
    order_id VARCHAR(50),
    order_date DATETIME,
    ship_mode VARCHAR(50),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales FLOAT,
    quantity INT,
    discount FLOAT,
    profit FLOAT
)
""")

conn.commit()

print("Orders table created")
