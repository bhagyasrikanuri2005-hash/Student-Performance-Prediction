import joblib
import pandas as pd

# Load trained classification model
model = joblib.load("classification_model.pkl")

print("====================================")
print("     Student Pass / Fail Predictor")
print("====================================")

# Study time
print("\nStudy Time:")
print("1 = Less than 2 hours/day")
print("2 = 2-5 hours/day")
print("3 = 5-10 hours/day")
print("4 = More than 10 hours/day")

studytime = int(input("\nEnter study time (1-4): "))

# First period grade
G1 = float(input("First period grade (G1) (0-20): "))

# Second period grade
G2 = float(input("Second period grade (G2) (0-20): "))

# Create input data
student = pd.DataFrame([{
    "studytime": studytime,
    "G1": G1,
    "G2": G2
}])

# Make prediction
prediction = model.predict(student)[0]

# Display result
print("\n====================================")

if prediction == 1:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")

print("====================================")