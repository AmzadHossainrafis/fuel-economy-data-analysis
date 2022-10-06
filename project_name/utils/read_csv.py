import pandas as pd

def read_csv(file_path):
    """
    Read csv file 
    return pandas dataframe
    """
    df = pd.read_csv(file_path)
    return df