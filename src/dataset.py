import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file and return it as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
