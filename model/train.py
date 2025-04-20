import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.metrics import mean_absolute_error
import joblib
data=pd.read_csv('C:/Users/hp/Desktop/house-price-predictor/data/Housing.csv', sep=',')
X = data.drop("price", axis=1)
y = np.log1p(data["price"])  

# Define categorical and numerical features
categorical_features = [
    'mainroad', 'guestroom', 'basement', 'hotwaterheating',
    'airconditioning', 'prefarea', 'furnishingstatus'
]
numerical_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

# Preprocessing steps
categorical_transformer = OneHotEncoder(drop='first', handle_unknown='ignore')

preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical_features)
], remainder='passthrough')  # Pass through numerical columns

# Build pipeline
pipeline = Pipeline(steps=[
    ('preprocessing', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42))
])


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
pipeline.fit(X_train, y_train)

# Predict and evaluate
y_pred_log = pipeline.predict(X_test)
y_pred = np.expm1(y_pred_log)  # Inverse log transform
true_values = np.expm1(y_test)

mae = mean_absolute_error(true_values, y_pred)
joblib.dump(pipeline, 'model/model.pkl')
print(f"✅ MAE: {mae:.2f}")