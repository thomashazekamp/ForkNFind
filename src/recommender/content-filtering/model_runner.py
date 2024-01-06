import pandas as pd
import numpy as np
from baseline_model import *
from sklearn_model import *

def main():

    business_data = pd.read_csv("../dataset/processed_dataset/business.csv")

    business_data.reset_index(inplace=True)
    business_data.index = business_data.index + 1

    baseline_score = baseline(business_data)

    sklearn_score_categorys = cosine_similarity_model_categorys(business_data)
    sklearn_score_attributes = cosine_similarity_model_attributes(business_data)
    sklearn_score_categorys_and_attributes = cosine_similarity_model_categorys_and_attributes(business_data)

    print(f'Baseline: {baseline_score}\nSklearn - Categorys: {sklearn_score_categorys}\nSklearn - Attributes: {sklearn_score_attributes}\nSklearn - Categorys & Attributes: {sklearn_score_categorys_and_attributes}')

main()