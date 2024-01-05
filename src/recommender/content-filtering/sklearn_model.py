import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def get_similar_items(row, cosine_similarity_matrix, train, test_ids):

    id = int(row[0])
    original_rating = row[1]
    
    item_similarities = cosine_similarity_matrix[id]

    top_similar_indices = item_similarities.argsort()[-20:][::-1]

    predicted_rating = []

    #print(id)
    #print(top_similar_indices)

    for item in top_similar_indices:

        #print(item)
        #print(item != id)
        #print(item not in test_ids)
        if item != id and item not in test_ids:
            result_row = train.loc[train['business_id'] == item]
            print(result_row)
            predicted_rating.append(result_row['stars'].item())

        # this represents the k nearest neighbour value
        if len(predicted_rating) == 5:
            break

    return sum(predicted_rating) / 5

def cosine_similarity_model(data):

    ratings = data[['business_id', 'stars']]

    rating_train, rating_test = train_test_split(ratings, test_size=0.2, random_state=42)

    rating_train.to_csv("rating_train.csv")
    rating_test.to_csv("rating_test.csv")

    feature_columns = data.columns.tolist()
    feature_columns = feature_columns[7:]

    features = data[feature_columns]

    features.to_csv("test.csv")
    
    cosine_similarity_matrix = cosine_similarity(features)

    new_ratings = []

    for index, row in rating_test.iterrows():
        print(index, row)
        new_ratings.append(get_similar_items(row, cosine_similarity_matrix, rating_train, rating_test['business_id']))

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)