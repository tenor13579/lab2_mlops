import pandas as pd
from sklearn.linear_model import Ridge
import pickle

def main():
    X_train = pd.read_csv("lab2/data/processed/X_train.csv")
    y_train = pd.read_csv("lab2/data/processed/y_train.csv")

    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    with open("lab2/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved.")

if __name__ == "__main__":
    main()