from surprise import Reader, Dataset, SVD, SVDpp, SlopeOne, NMF, KNNBaseline, KNNBasic, KNNWithMeans, KNNWithZScore, BaselineOnly, CoClustering
from surprise.model_selection import cross_validate, GridSearchCV
import pandas as pd

def surprise(data):

    reader = Reader(rating_scale=(1,5))

    data = Dataset.load_from_df(data[["user_id","business_id","stars"]], reader=reader)

    benchmark = []

    # Iterate over all algorithms
    for algorithm in [SVD(), SVDpp(), BaselineOnly(), SlopeOne(), NMF(), KNNBaseline(), KNNBasic(), KNNWithMeans(), KNNWithZScore(), CoClustering()]:
        # Perform cross validation
        results = cross_validate(algorithm, data, measures=['RMSE'], cv=3, verbose=False)
        
        # Get results & append algorithm name
        tmp = pd.DataFrame.from_dict(results).mean(axis=0)
        tmp = pd.concat([tmp, pd.Series([str(algorithm).split(' ')[0].split('.')[-1]], index=['Algorithm'])])
        benchmark.append(tmp)

    sorted_benchmark = sorted(benchmark, key=lambda df: df['test_rmse'])

    return sorted_benchmark[0]['test_rmse']


def surprise_hyperparameter(data):

    reader = Reader(rating_scale=(1,5))

    data = Dataset.load_from_df(data[["user_id","business_id","stars"]], reader=reader)

    param_grid = { 'bsl_options': 
        { 'method': ['als', 'sgd'],
        'ref': [0.05, 0.01, 0.02, 0.03],
        'learning_rate': [0.005, 0.01, 0.02],
        'n_epochs': [10, 15, 20, 30, 40]
    }}

    grid_search = GridSearchCV(BaselineOnly, param_grid, measures=['RMSE'], cv=5, n_jobs=-1)
    grid_search.fit(data)

    return grid_search.best_score["rmse"]