from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model/model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        features = {
            'area': int(request.form['area']),
            'bedrooms': int(request.form['bedrooms']),
            'bathrooms': int(request.form['bathrooms']),
            'stories': int(request.form['stories']),
            'mainroad': request.form['mainroad'],
            'guestroom': request.form['guestroom'],
            'basement': request.form['basement'],
            'hotwaterheating': request.form['hotwaterheating'],
            'airconditioning': request.form['airconditioning'],
            'parking': int(request.form['parking']),
            'prefarea': request.form['prefarea'],
            'furnishingstatus': request.form['furnishingstatus']
        }
        df = pd.DataFrame([features])
        prediction = model.predict(df)
        return f"<h2>Predicted Price: {round(prediction[0]):,} MAD</h2>"
    return render_template('index.html')
