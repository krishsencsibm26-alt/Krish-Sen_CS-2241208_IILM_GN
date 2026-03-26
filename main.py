import pandas as pd
from utils import summarize_data

def main():
    print("Running basic dataset experiment...")

    try:
        data = pd.read_csv("data_sample.csv")
        summarize_data(data)
    except FileNotFoundError:
        print("Dataset not found. Please check the file path.")

if __name__ == "__main__":
    main()
