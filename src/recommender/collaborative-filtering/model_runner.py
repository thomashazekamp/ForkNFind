from baseline_model import *
import pandas as pd

def main():

    review_data = pd.read_csv("../dataset/processed_dataset/review.csv")

    baseline(review_data)

main()