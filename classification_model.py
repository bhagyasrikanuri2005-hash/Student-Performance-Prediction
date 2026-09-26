import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# 1. Load dataset
data = pd.read_csv("dataset/student-mat.csv", sep=";")


# 2. Select useful features
# failures and absences are NOT used
features = ["studytime", "G1", "G2"]

X = data[features]


# 3. Create Pass/Fail target
# G3 >= 10  -> PASS (1)
# G3 < 10   -> FAIL (0)

y = (data["G3"] >= 10).astype(int)


# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 5. Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 6. Train model
model.fit(X_train, y_train)


# 7. Make predictions
predictions = model.predict(X_test)


# 8. Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# 9. Save model
joblib.dump(model, "classification_model.pkl")

print("Classification model saved successfully!")