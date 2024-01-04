from baseline_model import *
from fastai_model import *
from sklearn_model import *
from surprise_model import *
from lightfm_model import *
import pandas as pd

def main():

    review_data = pd.read_csv("../dataset/processed_dataset/review.csv")

    user_counts = review_data['user_id'].value_counts()
    filtered_user_ids = user_counts[user_counts > 25].index
    review_data = review_data[review_data['user_id'].isin(filtered_user_ids)]

    rating_1 = review_data[review_data["stars"] == 1]
    rating_2 = review_data[review_data["stars"] == 2]
    rating_3 = review_data[review_data["stars"] == 3]
    rating_4 = review_data[review_data["stars"] == 4]
    rating_5 = review_data[review_data["stars"] == 5]

    minimum_sample = min(review_data['stars'].value_counts())

    rating_1 = rating_1.sample(minimum_sample, random_state=42)
    rating_2 = rating_2.sample(minimum_sample, random_state=42)
    rating_3 = rating_3.sample(minimum_sample, random_state=42)
    rating_4 = rating_4.sample(minimum_sample, random_state=42)
    rating_5 = rating_5.sample(minimum_sample, random_state=42)
 
    balanced_df = pd.concat([rating_1,rating_2,rating_3,rating_4,rating_5])

    print(rating_1.shape)
    print(rating_2.shape)
    print(rating_3.shape)
    print(rating_4.shape)
    print(rating_5.shape)
    print(balanced_df.shape)

    baseline_score = baseline(balanced_df)
    fastai_score = fastai(balanced_df)
    sklearn_score = sklearn(balanced_df)
    surprise_score = surprise(balanced_df)
    lightfm_score = lightfm(balanced_df)

    print(lightfm_score)

    

    fast_ai_hyperparameter_score = fastai_hyperparameter(balanced_df)
    sklearn_hyperparameter_score = sklean_hyperparameter(balanced_df)
    lightfm_hyperparameter_score = lightfm_hyperparameter(balanced_df)

    print(lightfm_hyperparameter_score)

    print(f'Baseline: {baseline_score}\nFastAI: {fastai_score}\nSklearn: {sklearn_score}\nSurprise: {surprise_score}\nLightFM: {lightfm_score}')
    print(f'Hyperparameter Scores:')
    print(f'Baseline: {baseline_score}\nFastAI: {fast_ai_hyperparameter_score}\nSklearn: {sklearn_hyperparameter_score}\nSurprise: {surprise_score}\nLightFM: {lightfm_hyperparameter_score}')

main()