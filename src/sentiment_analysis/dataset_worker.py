import pandas as pd

def read_dataset():
    # Read in the data
    df = pd.read_csv('/dataset/tweet_data/tweet_data.csv')
    return df
