import pandas as pd
from surprise import Reader, Dataset, BaselineOnly
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


def start_collaborative_recommender():

    from .models import Review

    queryset = Review.objects.all()
    data = [{'user': item.get_user().get_id(), 'restaurant': item.get_restaurant().get_id(), 'rating': item.get_rating()} for item in queryset]
    review_dataframe = pd.DataFrame.from_records(data)

    reader = Reader(rating_scale=(1,5))

    surprise_data = Dataset.load_from_df(review_dataframe[["user","restaurant","rating"]], reader=reader)

    model = BaselineOnly()

    model.fit(surprise_data.build_full_trainset())

    return pickle.dumps(model)


def start_content_recommender():

    from .models import Restaurant, Category

    queryset = Restaurant.objects.all()
    queryset_categories = Category.objects.all()

    data_categories = [item for item in queryset_categories]

    data = []
    for item in queryset:

        item_data = {'restaurant_id': item.get_id(), 'allows_dogs': item.get_allows_dogs(), 'delivery': item.get_delivery(), 'dine_in': item.get_dine_in(), 'good_for_children': item.get_good_for_children(), 'good_for_groups': item.get_good_for_groups(), 'outfoor_seating': item.get_outdoor_seating()}

        for key, value in item_data.items():

            if type(value) == bool:
                if value == True:
                    item_data[key] = 1
                else:
                    item_data[key] = 0

        if item.get_price_level() == "PRICE_LEVEL_INEXPENSIVE":
            item_data['PRICE_LEVEL_INEXPENSIVE'] = 1
            item_data['PRICE_LEVEL_MODERATE'] = 0
            item_data['PRICE_LEVEL_EXPENSIVE'] = 0
        elif item.get_price_level() == "PRICE_LEVEL_MODERATE":
            item_data['PRICE_LEVEL_INEXPENSIVE'] = 0
            item_data['PRICE_LEVEL_MODERATE'] = 1
            item_data['PRICE_LEVEL_EXPENSIVE'] = 0
        elif item.get_price_level() == "PRICE_LEVEL_EXPENSIVE":
            item_data['PRICE_LEVEL_INEXPENSIVE'] = 0
            item_data['PRICE_LEVEL_MODERATE'] = 0
            item_data['PRICE_LEVEL_EXPENSIVE'] = 1

        item_categories = item.get_categories()

        for category in data_categories:
            if category in item_categories:
                item_data[category.get_category()] = 1
            else:
                item_data[category.get_category()] = 0
                     
        data.append(item_data)

    restaurant_dataframe = pd.DataFrame.from_records(data)

    feature_columns = restaurant_dataframe.columns.tolist()
    feature_columns = feature_columns[1:]

    features = restaurant_dataframe[feature_columns].copy()

    for col in features.columns:
        features[col] = features[col].apply(lambda value: "" if value == 0 else (col + " "))

    features['sentence'] = features.apply(lambda row: "".join(row), axis=1)

    features = features.drop(columns=features.columns[:-1])

    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(features['sentence'])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    masked_id_for_similarity = {}

    for index, row in restaurant_dataframe.iterrows():
        masked_id_for_similarity[int(row['restaurant_id'])] = int(index)

    return pickle.dumps(similarity_matrix), json.dumps(masked_id_for_similarity)

def get_content_recommendations(matrix, restaurant_id, restaurant_id_masking):

    restaurant_id_masking = json.loads(restaurant_id_masking)
    matrix = pickle.loads(matrix)

    masked_key = restaurant_id_masking[str(restaurant_id)]
    
    item_similarities = matrix[masked_key]

    top_similar_indices = item_similarities.argsort()[-4:][:3]

    real_ids = [[key for key, val in restaurant_id_masking.items() if val == value] for value in top_similar_indices]

    return [int(item) for sublist in real_ids for item in sublist]

def get_collaborative_recommendations(matrix, user_id):

    from .models import Review, Restaurant

    matrix = pickle.loads(matrix)

    queryset = Review.objects.filter(user=user_id)

    restaurant_ids = [item.get_restaurant().get_id() for item in queryset]
    
    restaurant_id_to_predict = Restaurant.objects.exclude(id__in=restaurant_ids)
    restaurant_id_to_predict = [item.get_id() for item in restaurant_id_to_predict]


    results = {}
    for id in restaurant_id_to_predict:
        results[id] = matrix.predict(user_id, id)[3]

    sorted_dict = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    return list(sorted_dict.keys())[:3]