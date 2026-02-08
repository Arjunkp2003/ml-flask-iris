from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df

def preprocess(df):
    # Iris dataset is clean
    return df

def save_processed_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['target'])
    train.to_csv("src/ml/train.csv", index=False)
    test.to_csv("src/ml/test.csv", index=False)
    print("Processed data saved.")
    return train, test

if __name__ == "__main__":
    df = load_data()
    df = preprocess(df)
    save_processed_data(df)
