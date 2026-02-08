import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model():
    df = pd.read_csv("src/ml/test.csv")
    X_test = df.drop("target", axis=1)
    y_test = df["target"]

    model = joblib.load("src/ml/model.pkl")
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model()
