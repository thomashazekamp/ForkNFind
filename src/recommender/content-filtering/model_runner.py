import pandas as pd
import numpy as np
from baseline_model import *
from sklearn_model import *

def main():

    business_data = pd.read_csv("../dataset/processed_dataset/business.csv")

    business_data.reset_index(inplace=True)
    business_data.index = business_data.index + 1

    baseline_score = baseline(business_data)

    sklearn_score = cosine_similarity_model(business_data)

    print(f'Baseline: {baseline_score}\nSklearn: {sklearn_score}')

main()