import pandas as pd

def load_data(filepath):
    """Load dataset."""
    df = pd.read_csv(filepath, encoding='unicode_escape')
    return df

def process_missing_data(df):
    """Process missing data by filling NA values."""
    df['location'] = df['location'].fillna(df['location'].mode()[0])
    df['type'] = df['type'].fillna(df['type'].mode()[0])
    df.fillna(0, inplace=True)
    return df

