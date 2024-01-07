import pandas as pd
import numpy as np
from baseline_model import *
from sklearn_model import *
from tfidf_model import *

def main():

    business_data = pd.read_csv("../dataset/processed_dataset/business.csv")

    business_data.reset_index(inplace=True)
    business_data.index = business_data.index + 1

    baseline_score = baseline(business_data)

    sklearn_score_categorys, sklearn_score_attributes, sklearn_score_categorys_and_attributes  = cosine_similarity_models(business_data)
    tfidf_score_categorys, tfidf_score_attributes, tfidf_score_categorys_and_attributes = tf_idf_similarity_models(business_data)

    print(f'Baseline: {baseline_score:.5f}\nSklearn - Categorys: {sklearn_score_categorys:.5f}\nSklearn - Attributes: {sklearn_score_attributes:.5f}\nSklearn - Categorys & Attributes: {sklearn_score_categorys_and_attributes:.5f}')
    print(f'Baseline: {baseline_score:.5f}\nTF-IDF - Categorys: {tfidf_score_categorys:.5f}\nTF-IDF - Attributes: {tfidf_score_attributes:.5f}\nTF-IDF - Categorys & Attributes: {tfidf_score_categorys_and_attributes:.5f}')

main()