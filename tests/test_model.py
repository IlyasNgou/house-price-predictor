import joblib
import pandas as pd

def test_prediction():
    model = joblib.load('model/model.pkl')
    test_input = pd.DataFrame([{
        'area': 3000, 'bedrooms': 3, 'bathrooms': 2, 'stories': 2,
        'mainroad': 'yes', 'guestroom': 'no', 'basement': 'yes',
        'hotwaterheating': 'no', 'airconditioning': 'yes',
        'parking': 2, 'prefarea': 'yes', 'furnishingstatus': 'furnished'
    }])
    prediction = model.predict(test_input)
    assert prediction[0] > 0
