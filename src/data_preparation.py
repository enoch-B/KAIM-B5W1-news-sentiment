import pandas as pd

def load_stock_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df

