import pytest
import pandas as pd
from src.ml.predict import make_prediction
from src.ml.train import train_model
from src.ml.preprocess import preprocess, load_data, save_processed_data

def test_model_pipeline():
    # Load and preprocess data
    df = load_data()
    df = preprocess(df)
    save_processed_data(df)

    # Train model
    train_model()

    # Test prediction
    sample_input = {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2
    }
    prediction = make_prediction(sample_input)
    assert prediction in [0, 1, 2], "Prediction should be a valid Iris class"
