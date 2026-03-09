import pandas as pd

# Load dataset
df = pd.read_csv("EcommerceData/data.csv", encoding="latin1")

print("Original Rows:", len(df))

# Remove missing values
df = df.dropna(subset=["CustomerID", "Description"])

# Remove negative quantities
df = df[df["Quantity"] > 0]

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("Cleaned Rows:", len(df))

# Save cleaned dataset
df.to_csv("cleaned_ecommerce_data.csv", index=False)

print("Cleaned dataset saved!")
