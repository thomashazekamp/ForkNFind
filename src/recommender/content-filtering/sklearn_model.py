import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def get_similar_items(row, cosine_similarity_matrix, train, test_ids):

    id = int(row[0])
    
    item_similarities = cosine_similarity_matrix[id]

    top_similar_indices = item_similarities.argsort()[-20:][::-1]

    predicted_rating = []

    for item in top_similar_indices:

        if item != id and item not in test_ids and item != 0:
            if item not in test_ids:
                result_row = train.loc[train['business_id'] == item]
                predicted_rating.append(result_row['stars'].item())

        # this represents the k nearest neighbour value
        if len(predicted_rating) == 7:
            break

    return sum(predicted_rating) / 7

def compute_similarity_and_loop(data, rating_train, rating_test, feature_columns):

    features = data[feature_columns]
   
    cosine_similarity_matrix = cosine_similarity(features)

    new_ratings = []

    for _, row in rating_test.iterrows():
        new_ratings.append(get_similar_items(row, cosine_similarity_matrix, rating_train, rating_test['business_id']))

    return new_ratings


def cosine_similarity_model_categorys(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[7:46]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def cosine_similarity_model_attributes(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[46:]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def cosine_similarity_model_categorys_and_attributes(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[7:]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def cosine_similarity_models(data):

    ratings = data[['business_id', 'stars']]

    rating_train, rating_test = train_test_split(ratings, test_size=0.2, random_state=38)

    feature_columns = data.columns.tolist()

    sklearn_score_categorys = cosine_similarity_model_categorys(data, rating_train, rating_test, feature_columns)
    sklearn_score_attributes = cosine_similarity_model_attributes(data, rating_train, rating_test, feature_columns)
    sklearn_score_categorys_and_attributes = cosine_similarity_model_categorys_and_attributes(data, rating_train, rating_test, feature_columns)


    return sklearn_score_categorys, sklearn_score_attributes, sklearn_score_categorys_and_attributes 