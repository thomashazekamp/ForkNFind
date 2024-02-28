'''
References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''
import pandas as pd
from txt_processing import process_text

# Read in the data
def read_dataset():
    # Read in the data
    dataset = 'dataset/yelp_review_polarity_dataset/updated_yelp_polarity_train.csv'
    df = pd.read_csv(dataset)
    df = df.head(5000) # Limiting the dataset to a number of rows for memory purposes

    return df

def apply_dataset_column_modifications(df): # applies the new processed text to the dataset. i.e adds processed tokens (adds column) calling the process_text function and changes the sentiment to 1 or 0
    # apply the process_text function to the tweet_text column
    df["tokens"] = df["text"].apply(process_text)

    # change sentiment to 1 or 0
    df["text_sentiment"] = df["sentiment"].apply(lambda x: 1 if x == "positive" else 0)

    return df

# Convert the dataset to lists
def dataset_tolist(df):
    x  = df["tokens"].tolist()
    y = df["text_sentiment"].tolist()

    return x, y
