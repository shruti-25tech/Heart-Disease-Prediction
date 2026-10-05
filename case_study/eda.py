import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/heart.csv")

# Remove duplicate rows for analysis
df = df.drop_duplicates()

print("Dataset shape after removing duplicates:", df.shape)

# Target distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="target", data=df)
plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease (0 = No, 1 = Yes)")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Age distribution
plt.figure(figsize=(7, 4))
sns.histplot(df["age"], bins=15, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Cholesterol distribution
plt.figure(figsize=(7, 4))
sns.histplot(df["chol"], bins=20, kde=True)
plt.title("Cholesterol Distribution")
plt.xlabel("Cholesterol")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Heart disease by chest pain type
plt.figure(figsize=(7, 4))
sns.countplot(x="cp", hue="target", data=df)
plt.title("Heart Disease by Chest Pain Type")
plt.xlabel("Chest Pain Type")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()