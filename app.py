from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML model
model = joblib.load("classification_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    studytime = int(data["studytime"])
    G1 = float(data["G1"])
    G2 = float(data["G2"])

    # Create input data
    student = pd.DataFrame([{
        "studytime": studytime,
        "G1": G1,
        "G2": G2
    }])

    # Make prediction
    prediction = model.predict(student)[0]

    if prediction == 1:
        result = "PASS"
    else:
        result = "FAIL"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)