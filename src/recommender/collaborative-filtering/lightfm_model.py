
from lightfm.cross_validation import random_train_test_split
from sklearn.preprocessing import MinMaxScaler
import scipy.sparse as sp
from lightfm import LightFM
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt



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