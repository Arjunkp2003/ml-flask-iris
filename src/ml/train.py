import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("src/ml/train.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, "src/ml/model.pkl")
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_model()
