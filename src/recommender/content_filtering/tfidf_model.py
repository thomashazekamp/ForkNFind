from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

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

    features = data[feature_columns].copy()

    for col in features.columns:
        features[col] = features[col].apply(lambda value: "" if value == 0 else (col + " "))

    features['sentence'] = features.apply(lambda row: "".join(row), axis=1)

    features = features.drop(columns=features.columns[:-1])

    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(features['sentence'])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    new_ratings = []


    for _, row in rating_test.iterrows():
        new_ratings.append(get_similar_items(row, similarity_matrix, rating_train, rating_test['business_id']))

    return new_ratings


def tfidf_model_categorys(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[7:46]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def tfidf_model_attributes(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[46:]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def tfidf_model_categorys_and_attributes(data, rating_train, rating_test, feature_columns):

    feature_columns = feature_columns[7:]

    new_ratings = compute_similarity_and_loop(data, rating_train, rating_test, feature_columns)

    return mean_squared_error(new_ratings, rating_test['stars'], squared=False)


def tf_idf_similarity_models(data):

    ratings = data[['business_id', 'stars']]

    rating_train, rating_test = train_test_split(ratings, test_size=0.2, random_state=38)

    feature_columns = data.columns.tolist()

    tfidf_model_categorys_result = tfidf_model_categorys(data, rating_train, rating_test, feature_columns)
    tfidf_score_attributes_result = tfidf_model_attributes(data, rating_train, rating_test, feature_columns)
    tfidf_score_categorys_and_attributes_result = tfidf_model_categorys_and_attributes(data, rating_train, rating_test, feature_columns)

    return tfidf_model_categorys_result, tfidf_score_attributes_result, tfidf_score_categorys_and_attributes_result 