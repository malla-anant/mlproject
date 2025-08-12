## End to End Machine Learning Project

# 🎯 Student Exam Performance Prediction

This project predicts a student’s **Math Score** based on features such as gender, race/ethnicity, parental education, lunch type, test preparation course, and other scores.  
It uses **Machine Learning** and serves predictions through a **Flask web application**.

## 📌 Features
- Predicts math scores from student background and test data.
- End-to-end ML pipeline:
  - Data ingestion
  - Data transformation
  - Model training & evaluation
- Best model saved for deployment.
- Flask web app for real-time predictions.

## 🖥️ Demo

<img width="574" height="307" alt="Screenshot 2025-08-12 172340" src="https://github.com/user-attachments/assets/014ccb3b-0f45-430d-ab8b-5ebd9caf73d0" />

## 📂 Project Structure

mlproject/

│

├── app.py # Flask application entry point

├── src/

│ ├── components/ # Data transformation & model trainer

│ ├── pipeline/ # Training & prediction pipelines

│ ├── utils.py # Utility functions

│ ├── logger.py # Logging setup

│ ├── exception.py # Custom exception handling

│

├── artifacts/ # Saved models & preprocessors

├── templates/ # HTML templates for Flask app

├── requirements.txt # Project dependencies

└── README.md


## ⚙️ Installation & Setup

**Clone the repository**

git clone https://github.com/malla-anant/mlproject.git
cd mlproject
Create & activate virtual environment
python -m venv venv
### Windows:
venv\Scripts\activate
### Linux/Mac:
source venv/bin/activate
### Install dependencies
pip install -r requirements.txt
### Run training pipeline
python -m src.pipeline.train_pipeline
### Run Flask app
python app.py
Access the app at http://127.0.0.1:5000

## 📊 Model Training

Multiple regression models were tested (Linear Regression, CatBoost, XGBoost, etc.).

Best model: Linear Regression with R² score ≈ 0.88.

## 📦 Technologies Used

Python 3.12, Pandas, NumPy, Scikit-learn, Flask, CatBoost / XGBoost, HTML
