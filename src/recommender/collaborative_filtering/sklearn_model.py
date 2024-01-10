from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
from math import sqrt


def sklearn(data):

    information = data[['user_id', 'business_id']]
    rating = data['stars']

    info_train, info_test, rating_train, rating_test = train_test_split(information, rating, test_size=0.2, random_state=42)

    model = KNeighborsRegressor(n_neighbors=5)

    model.fit(info_train, rating_train)

    predictions = model.predict(info_test)

    rmse = np.sqrt(mean_squared_error(rating_test, predictions))
    
    return rmse

def sklean_hyperparameter(data):

    information = data[['user_id', 'business_id']]
    rating = data['stars']

    param_grid = {
        'n_neighbors': [3, 5],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
        'leaf_size': [10, 20, 30],
        'metric': ['euclidean', 'manhattan']
    }

    info_train, info_test, rating_train, rating_test = train_test_split(information, rating, test_size=0.2, random_state=42)

    model = KNeighborsRegressor()

    scorer = make_scorer(lambda y_true, y_pred: -sqrt(mean_squared_error(y_true, y_pred)))

    # Perform grid search
    grid_search = GridSearchCV(model, param_grid, scoring=scorer, cv=5)
    grid_search.fit(info_train, rating_train)

    # Get the best model from the grid search
    best_knn_regressor = grid_search.best_estimator_

    # Make predictions on the test set
    y_pred = best_knn_regressor.predict(info_test)

    # Calculate RMSE
    rmse = sqrt(mean_squared_error(rating_test, y_pred))

    return rmse