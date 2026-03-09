import pandas as pd

# Load dataset
df = pd.read_csv("EcommerceData/data.csv", encoding="latin1")

print("\nTotal Records:", len(df))

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())
