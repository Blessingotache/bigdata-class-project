import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.drop_duplicates().dropna()
    return df

def save_cleaned(df, output_path):
    df.to_csv(output_path, index=False)
