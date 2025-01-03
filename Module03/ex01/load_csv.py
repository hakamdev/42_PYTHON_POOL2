import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a CSV file and returns its data as a DataFrame object
    Args:
        path: path to the csv file
    """
    if (type(path) is not str):
        print("AssertionError: Invalid path")
        return None
    if (path is None or path == ""):
        print("AssertionError: Empty path")
        return None
    path_segments = path.lower().split(".")
    if (len(path_segments) < 2):
        print("AssertionError: Invalid path")
        return None
    extension = path_segments[-1]
    if (extension != "csv"):
        print("AssertionError: Invalid path")
        return None
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"AssertionError: No such file or directory: '{path}'")
        return None
    except Exception:
        print(f"AssertionError: failed to load: {path}")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df
