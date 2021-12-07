from flask import Flask, redirect, url_for, render_template, request

# Data Wrangling and Data Analysis
import pandas as pd , numpy as np

# Model Building
import pickle

# Initialize Flask APP
app = Flask(__name__)

# Load Model
model = pickle.load(open('pima_model', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    return render_template('analysis.html')

@app.route('/predict', methods=['POST'])
def predict():
    Features = [float(x) for x in request.form.values()]
    Features = [np.array(Features)]
    Prediction = str(model.predict(Features)[0])

    if Prediction == "1":
        Prediction = "Patient is Diabetic ! \N{pensive face}"
    else:
        Prediction = "Patient is Non-Diabetic !  \N{slightly smiling face}"
    
    return render_template('index.html',Prediction = Prediction)

if __name__ == '__main__':
    app.run(debug=True)