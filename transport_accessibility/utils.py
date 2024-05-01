import pandas as pd

def save_df_to_csv(df: pd.DataFrame, file_path: str):
    """
    Saves a DataFrame to a CSV file.
    """
    df.to_csv(file_path, index=False)