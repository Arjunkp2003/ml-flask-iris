import joblib
import pandas as pd

model = joblib.load("src/ml/model.pkl")

def make_prediction(input_dict):
    df = pd.DataFrame([input_dict])
    prediction = model.predict(df)[0]
    return int(prediction)
