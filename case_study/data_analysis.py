import pandas as pd

# Load dataset
df = pd.read_csv("data/heart.csv")

# Display basic information
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

print("\n--- TARGET DISTRIBUTION ---")

# Change 'target' if your dataset uses a different target column
if "target" in df.columns:
    print(df["target"].value_counts())
else:
    print("Target column not found.")