import pandas as pd
import pickle
from sklearn.metrics import root_mean_squared_error

def main():
    X_test = pd.read_csv("lab2/data/processed/X_test.csv")
    y_test = pd.read_csv("lab2/data/processed/y_test.csv")

    with open("lab2/model.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, y_pred)

    print(f"Model RMSE: {rmse:.4f}")

if __name__ == "__main__":
    main()