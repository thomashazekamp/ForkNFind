import pandas as pd
import numpy as np
from baseline_model import *

def main():

    business_data = pd.read_csv("../dataset/processed_dataset/business.csv")

    business_data.reset_index(inplace=True)

    baseline_score = baseline(business_data)

    print(f'Baseline: {baseline_score}\n')

main()