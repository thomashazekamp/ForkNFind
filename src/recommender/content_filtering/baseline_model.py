import pandas as pd
from sklearn.model_selection import train_test_split
import random
import math

def content_filtering_baseline(data):

    rating = data['stars']

    rating_train, rating_test = train_test_split(rating, test_size=0.2, random_state=42)

    value_counts = {}

    for value in rating_train:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    total_count = sum(value_counts.values())
    value_percentages = {key: (count / total_count) * 100 for key, count in value_counts.items()}

    predictions = random.choices(list(value_percentages.keys()), weights=value_percentages.values(), k=len(rating_test))

    squared_errors = [(prediction - actual)**2 for prediction, actual in zip(predictions, rating_test)]
    mean_squared_error = sum(squared_errors) / len(predictions)
    rmse = math.sqrt(mean_squared_error)

    return rmse