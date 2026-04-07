import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    os.makedirs("lab2/data/processed", exist_ok=True)

    df = pd.read_csv("lab2/data/raw/diabetes.csv")

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    pd.DataFrame(X_train_scaled).to_csv("lab2/data/processed/X_train.csv", index=False)
    pd.DataFrame(X_test_scaled).to_csv("lab2/data/processed/X_test.csv", index=False)
    y_train.to_csv("lab2/data/processed/y_train.csv", index=False)
    y_test.to_csv("lab2/data/processed/y_test.csv", index=False)

    print("Preprocessing done.")

if __name__ == "__main__":
    main()