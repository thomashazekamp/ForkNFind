'''
References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''
import pandas as pd
from txt_processing import process_text

def read_dataset():
    # Read in the data
    df = pd.read_csv('dataset/tweet_data/tweet_data.csv')
    # df = df.head(100) # Limiting the dataset to 100 rows for testing purposes

    return df

def apply_dataset_column_modifications(df): # applies the new processed text to the dataset. i.e adds processed tokens (adds column) calling the process_text function and changes the sentiment to 1 or 0
    # apply the process_text function to the tweet_text column
    df["tokens"] = df["tweet_text"].apply(process_text)

    # change sentiment to 1 or 0
    df["tweet_sentiment"] = df["sentiment"].apply(lambda x: 1 if x == "positive" else 0)

    return df

def dataset_tolist(df):
    x  = df["tokens"].tolist()
    y = df["tweet_sentiment"].tolist()

    return x, y
