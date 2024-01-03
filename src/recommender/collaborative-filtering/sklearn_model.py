from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
import numpy as np


def sklearn(data):

    information = data[['user_id', 'business_id']]
    rating = data['stars']

    info_train, info_test, rating_train, rating_test = train_test_split(information, rating, test_size=0.2, random_state=42)

    model = KNeighborsRegressor(n_neighbors=5)

    model.fit(info_train, rating_train)

    predictions = model.predict(info_test)

    rmse = np.sqrt(mean_squared_error(rating_test, predictions))
    
    return rmse