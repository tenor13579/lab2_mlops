import os
import pandas as pd
from sklearn.datasets import load_diabetes

def main():
    os.makedirs("lab2/data/raw", exist_ok = True)
    data = load_diabetes(as_frame = True)
    df = data.frame
    df.to_csv("lab2/data/raw/diabetes.csv", index = False)
    print("Le dataset est bien enregistre")

if __name__ == "__main__":
    main()