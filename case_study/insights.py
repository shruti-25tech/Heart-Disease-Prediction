import pandas as pd

# Load dataset
df = pd.read_csv("data/heart.csv")

# Remove duplicate rows
df = df.drop_duplicates()

print("\n--- DATASET INSIGHTS ---")

print("\n1. Total patients:", len(df))

print("\n2. Average age:", round(df["age"].mean(), 2))

print("\n3. Average cholesterol:", round(df["chol"].mean(), 2))

print("\n4. Average resting blood pressure:",
      round(df["trestbps"].mean(), 2))

print("\n5. Heart disease distribution:")
print(df["target"].value_counts())

print("\n6. Heart disease percentage:")
print((df["target"].value_counts(normalize=True) * 100).round(2))

print("\n7. Heart disease by chest pain type:")
print(pd.crosstab(df["cp"], df["target"]))

print("\n8. Heart disease by gender:")
print(pd.crosstab(df["sex"], df["target"]))

print("\n--- CASE STUDY CONCLUSION ---")
print("The dataset contains patient health information used")
print("to analyze factors associated with heart disease.")
print("The cleaned dataset will be used for machine learning.")