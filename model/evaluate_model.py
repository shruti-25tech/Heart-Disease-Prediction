import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load dataset
df = pd.read_csv("data/heart.csv")

# Remove duplicates
df = df.drop_duplicates()

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load saved scaler and model
with open("model/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("model/heart_model.pkl", "rb") as file:
    model = pickle.load(file)

# Scale test data
X_test = scaler.transform(X_test)

# Make predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\n--- MODEL EVALUATION ---")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))