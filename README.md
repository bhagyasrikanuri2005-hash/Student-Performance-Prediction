# Student Performance Prediction

🔗 **Live Demo:** [Student Performance Predictor](https://student-performance-prediction-lajy.onrender.com)

A Machine Learning web application that predicts a student's academic result based on study time and previous period grades.

## 📌 Project Overview

Student Performance Predictor is a Flask-based Machine Learning application designed to estimate whether a student is likely to **PASS or FAIL** based on selected academic inputs.

The application uses a trained Machine Learning classification model to generate the prediction and displays the result through a simple and user-friendly web interface.

## ✨ Features

- 📚 Study time selection
- 📝 First Period Grade (G1) input
- 📝 Second Period Grade (G2) input
- 🤖 Machine Learning based prediction
- ✅ PASS / ❌ FAIL result
- 🌐 Flask web application
- 🎨 Simple and responsive user interface

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS
- Git & GitHub

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── dataset/
│   └── student-mat.csv
│
├── static/
│   ├── study-bg.jpg
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── classification_model.py
├── classification_predict.py
├── classification_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. The user opens the Student Performance Predictor web application.
2. The user selects the study time from the dropdown.
3. The user enters the First Period Grade (G1).
4. The user enters the Second Period Grade (G2).
5. The entered data is sent to the Flask backend.
6. The trained Machine Learning classification model processes the input data.
7. The model predicts whether the student is likely to PASS or FAIL.
8. The prediction result is displayed on the web page.

## 🧠 Machine Learning

The project uses a Machine Learning classification model trained using student academic data.

### Input Features

- Study Time
- First Period Grade (G1)
- Second Period Grade (G2)

### Output

- PASS
- FAIL

The trained model is saved as:

`classification_model.pkl`

## 📁 Main Files

- `app.py` – Flask application and backend
- `classification_model.py` – Machine Learning model training
- `classification_predict.py` – Prediction logic
- `classification_model.pkl` – Trained Machine Learning model
- `dataset/student-mat.csv` – Student dataset
- `templates/index.html` – Frontend page
- `static/style.css` – Application styling
- `static/study-bg.jpg` – Study-themed background image
- `requirements.txt` – Required Python libraries
- `.gitignore` – Files and folders excluded from Git tracking
- `README.md` – Project documentation

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/bhagyasrikanuri2005-hash/Student-Performance-Prediction.git
```

### 2. Open the project folder

```bash
cd Student-Performance-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install required libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application

```bash
python app.py
```

### 7. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 📊 Example

Example input:

- Study Time: Less than 2 hours/week
- G1: 15
- G2: 16

The application processes these values using the trained classification model and displays the predicted result.

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be integrated with a Flask web application to predict student academic results based on study time and previous grades.

## 🚀 Future Improvements

- Add more student-related features
- Improve model performance using different Machine Learning algorithms
- Display prediction probability
- Add student performance visualizations
- Add student performance history
- Deploy the application online using a cloud platform such as AWS

## 👩‍💻 Author

**Bala Bhagya Sri Kanuri**

B.Tech – Computer Science & Engineering

GitHub: https://github.com/bhagyasrikanuri2005-hash

---

⭐ If you find this project useful, consider giving it a star!
