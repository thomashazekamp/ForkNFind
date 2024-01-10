
from lightfm.cross_validation import random_train_test_split
from sklearn.preprocessing import MinMaxScaler
import scipy.sparse as sp
from lightfm import LightFM
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
from itertools import product



def build_and_test_dataset(data, model):

    manual_interactions = sp.coo_matrix((data['stars'], (data['user_id'], data['business_id'])))

    train_data, test_data = random_train_test_split(manual_interactions, test_percentage=0.2, random_state=42)

    model = LightFM(loss=model)

    # Train the model
    model.fit(train_data, epochs=30, num_threads=2)

    predictions = model.predict(test_data.row, test_data.col)

    # Reshape the values to a 2D array (required by MinMaxScaler)
    original_values_2d = np.array(predictions).reshape(-1, 1)

    # Create and fit the scaler with a custom feature range [1, 5]
    scaler = MinMaxScaler(feature_range=(1, 5))
    scaler.fit(original_values_2d)

    normalized_values = scaler.transform(original_values_2d).flatten()

    # Calculate RMSE
    rmse = sqrt(mean_squared_error(test_data.data, normalized_values))

    return rmse

def lightfm(data):

    warp_score = build_and_test_dataset(data, "warp")

    logitstic_score = build_and_test_dataset(data, "logistic")

    bpr_score = build_and_test_dataset(data, "bpr")

    return min(warp_score, logitstic_score, bpr_score)

def get_rmse(line):
    return float(line.split('- RMSE: ')[1])

def grid_search(no_components_values, learning_rate_values, item_alpha_values, user_alpha_values, epochs_values, loss_values, data, results):
    
    for no_components, learning_rate, item_alpha_values, user_alpha_values, epochs_values, loss_function in product(no_components_values, learning_rate_values, item_alpha_values, user_alpha_values, epochs_values, loss_values):
    
        manual_interactions = sp.coo_matrix((data['stars'], (data['user_id'], data['business_id'])))

        train_data, test_data = random_train_test_split(manual_interactions, test_percentage=0.2, random_state=42)
        model = LightFM(
            loss=loss_function,
            no_components=no_components,
            learning_rate=learning_rate,
            item_alpha=item_alpha_values,
            user_alpha=user_alpha_values,
            random_state=42,
        )

        # Train the model
        model.fit(train_data, epochs=epochs_values, num_threads=4)


        predictions = model.predict(test_data.row, test_data.col)

        # Reshape the values to a 2D array (required by MinMaxScaler)
        original_values_2d = np.array(predictions).reshape(-1, 1)

        # Create and fit the scaler with a custom feature range [1, 5]
        scaler = MinMaxScaler(feature_range=(1, 5))
        scaler.fit(original_values_2d)

        normalized_values = scaler.transform(original_values_2d).flatten()

        # Calculate RMSE
        rmse = sqrt(mean_squared_error(test_data.data, normalized_values))

        results.append(f"no_components={no_components}, learning_rate={learning_rate}, item_alpha_values={item_alpha_values}, user_alpha_values={user_alpha_values}, epochs_values={epochs_values} - RMSE: {rmse}")


def lightfm_hyperparameter(data):

    results = []

    no_components_values = [30, 50, 64]  # Adjust the dimensionality of latent vectors
    learning_rate_values = [0.01, 0.05, 0.1]  # Learning rate for optimization
    item_alpha_values = [0.0001, 0.001, 0.01]  # Item regularization strength
    user_alpha_values = [0.0001, 0.001, 0.01]  # User regularization strength
    epochs_values = [20, 30, 40]  # Number of training epochs
    loss_values = ['warp', 'logistic', 'bpr', 'warp-kos']

    # Perform grid search
    grid_search(no_components_values, learning_rate_values, item_alpha_values, user_alpha_values, epochs_values, loss_values, data, results)

    sorted_lines = sorted(results, key=get_rmse)

    return sorted_lines[0].split('- RMSE: ')[1]