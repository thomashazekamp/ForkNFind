import pandas as pd
from surprise import Reader, Dataset, BaselineOnly
import pickle


def start_collaborative_recommender():

    from .models import Review

    queryset = Review.objects.all()
    data = [{'user': item.user.get_id(), 'restaurant': item.restaurant.get_id(), 'rating': item.rating} for item in queryset]
    review_dataframe = pd.DataFrame.from_records(data)

    reader = Reader(rating_scale=(1,5))

    surprise_data = Dataset.load_from_df(review_dataframe[["user","restaurant","rating"]], reader=reader)

    model = BaselineOnly()

    model.fit(surprise_data.build_full_trainset())

    return pickle.dumps(model)