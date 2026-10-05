import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv("data/heart.csv")

# Remove duplicate rows
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

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression(random_state=42)

model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model training completed successfully.")
print("Logistic Regression Accuracy:", round(accuracy * 100, 2), "%")

# Save model
with open("model/heart_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save scaler
with open("model/scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

print("Model saved as model/heart_model.pkl")
print("Scaler saved as model/scaler.pkl")