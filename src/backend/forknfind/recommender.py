import pandas as pd
from surprise import Reader, Dataset, BaselineOnly
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# function to initialise the collaborative recommender model
def start_collaborative_recommender():

    # imports the review class
    from .models import Review

    # gets all reviews from the database
    queryset = Review.objects.all()
    # convert them to the format that is required
    data = [{'user': item.get_user().get_id(), 'restaurant': item.get_restaurant().get_id(), 'rating': item.get_rating()} for item in queryset]
    # put the review data into a dataframe
    review_dataframe = pd.DataFrame.from_records(data)

    # create the reader to set the scale ratings must be between
    reader = Reader(rating_scale=(1,5))

    # load the dataframe into a surprise dataset
    surprise_data = Dataset.load_from_df(review_dataframe[["user","restaurant","rating"]], reader=reader)

    # initialise the machine learning model
    model = BaselineOnly()

    # fit the full dataset to the model
    model.fit(surprise_data.build_full_trainset())

    # return the model but using pickle.dump() to convert it to binary
    return pickle.dumps(model)


def start_content_recommender():

    # imports the restaurant and category classes
    from .models import Restaurant, Category

    # gets all restaurants from the database
    queryset = Restaurant.objects.all()
    # gets all categorys from the database
    queryset_categories = Category.objects.all()

    # convert the categories to a list
    data_categories = [item for item in queryset_categories]

    data = []
    # loop throuhg the restaurant queryset, to convert it into the correct format
    for item in queryset:

        # convert the attributes the correct format
        item_data = {'restaurant_id': item.get_id(), 'allows_dogs': item.get_allows_dogs(), 'delivery': item.get_delivery(), 'dine_in': item.get_dine_in(), 'good_for_children': item.get_good_for_children(), 'good_for_groups': item.get_good_for_groups(), 'outfoor_seating': item.get_outdoor_seating()}

        # for all boolean attributes if the value is "True" then convert the value to 1, this is one-hot encoding, if not a "True" then put the value as 0
        for key, value in item_data.items():

            if type(value) == bool:
                if value == True:
                    item_data[key] = 1
                else:
                    item_data[key] = 0

        # checks to see which price level appears, whichever appears gets a 1 and the others a 0
        if item.get_price_level() == "low":
            item_data['low'] = 1
            item_data['medium'] = 0
            item_data['high'] = 0
        elif item.get_price_level() == "medium":
            item_data['low'] = 0
            item_data['medium'] = 1
            item_data['high'] = 0
        elif item.get_price_level() == "high":
            item_data['low'] = 0
            item_data['medium'] = 0
            item_data['high'] = 1

        # get the categories for the restaurant
        item_categories = item.get_categories()

        # loop through categories and for each that appears set the value to 1 and if it doesnt appear set to 0
        for category in data_categories:
            if category in item_categories:
                item_data[category.get_category()] = 1
            else:
                item_data[category.get_category()] = 0
                     
        # add the restaurant data to list
        data.append(item_data)

    # convert list of restaurants to dataframe
    restaurant_dataframe = pd.DataFrame.from_records(data)

    # get all feature columns to caluclate similarity, except the first one which is the restaurant id
    feature_columns = restaurant_dataframe.columns.tolist()
    feature_columns = feature_columns[1:]

    features = restaurant_dataframe[feature_columns].copy()

    # loop through converting where appears to the name of the column and when 0 appears to ""
    for col in features.columns:
        features[col] = features[col].apply(lambda value: "" if value == 0 else (col + " "))

    # join all columns into a sentence, where tf-idf can be used on it
    features['sentence'] = features.apply(lambda row: "".join(row), axis=1)

    features = features.drop(columns=features.columns[:-1])

    # initialise tf-idf 
    tfidf_vector = TfidfVectorizer()
    # use it own the sentence column
    tfidf_matrix = tfidf_vector.fit_transform(features['sentence'])
    # use cosine simialirty on the matrix to see how similar restaurants are
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    masked_id_for_similarity = {}

    # convert ids of restaurants to a new index so it starts from 0 and ends on the last one
    for index, row in restaurant_dataframe.iterrows():
        masked_id_for_similarity[int(row['restaurant_id'])] = int(index)

    # dump the data so it can be saved to database
    return pickle.dumps(similarity_matrix), json.dumps(masked_id_for_similarity)

# function for querying the content recommender, takes an input of the matrix, restaurant_id and restaurant_id maskings
def get_content_recommendations(matrix, restaurant_id, restaurant_id_masking):

    # load the data from what was saved into the database to the original format
    restaurant_id_masking = json.loads(restaurant_id_masking)
    matrix = pickle.loads(matrix)

    # get the masked key of the restaurant_id passed in 
    masked_key = restaurant_id_masking[str(restaurant_id)]
    
    # get all similarites for that restaurant
    item_similarities = matrix[masked_key]

    # take the top 4 restaurants and then lost the first 1 as the first 1 will be itself
    top_similar_indices = item_similarities.argsort()[-4:][:3]

    # get the real ideas of each of the top_similar_indices
    real_ids = [[key for key, val in restaurant_id_masking.items() if val == value] for value in top_similar_indices]

    # return the ids so they are all in 1 list
    return [int(item) for sublist in real_ids for item in sublist]

# function for querying the collaborative recommender, takes an input of the matrix and user_id
def get_collaborative_recommendations(matrix, user_id):

    # imports the restaurant and category classes
    from .models import Review, Restaurant

    # load the data from what was saved into the database to the original format
    matrix = pickle.loads(matrix)

    # filter all reviews just for the ones made by current user
    queryset = Review.objects.filter(user=user_id)

    # get all the restaurant ids for those reviews
    restaurant_ids = [item.get_restaurant().get_id() for item in queryset]
    
    # get the queryset of restaurants to predict excluding those already reviewed by the user
    restaurant_id_to_predict = Restaurant.objects.exclude(id__in=restaurant_ids)
    restaurant_id_to_predict = [item.get_id() for item in restaurant_id_to_predict]


    results = {}
    # for each restaurant loop through and predict what the user would rate
    for id in restaurant_id_to_predict:
        results[id] = matrix.predict(user_id, id)[3]

    # sort the list of predicitons
    sorted_dict = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # return the keys of each of the 3 highest predictions in a list format
    return list(sorted_dict.keys())[:3]

# function for querying the collaborative recommended, takes an input of the matrix, user_id and restaurants to predict their ratings
def get_collaborative_recommender_from_list(matrix, user_id, restaurant_id_list):

    # load the data from what was saved into the database to the original format
    matrix = pickle.loads(matrix)

    # where all the results will be held
    results = {}

    # for each restaurant loop through and predict what the user would rate
    for item in restaurant_id_list:
        results[item] = matrix.predict(user_id, item)

    # sort the list of predicitons
    sorted_dict = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # return the keys of the highest 10% of restaurant predictions
    return list(sorted_dict.keys())[:(len(sorted_dict)//10)]
    