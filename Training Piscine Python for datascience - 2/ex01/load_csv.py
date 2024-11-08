import pandas as pd
import os as os


def load(path: str) -> pd.DataFrame:
    """
    Print the dimension of data set and return it.

    Args :
        path (str) : The path of the csv data set.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File not found.")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file is not in csv extension.")

        dataset = pd.read_csv(path)

        if dataset.empty:
            raise AssertionError("The csv file is empty.")

        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset
    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")

        return None
