from sklearn.model_selection import train_test_split
from fastai.tabular.all import *
from fastai.collab import *
import warnings
from itertools import product


def fastai(data):

    warnings.filterwarnings("ignore", category=UserWarning, module="fastai.torch_core")

    train, test = train_test_split(data, test_size=0.2, random_state=42)

    # Creates the data loader for the collaborative filtering
    dls = CollabDataLoaders.from_df(train, bs=64)

    # Creating the collaborative filtering learner with parameters
    learn = collab_learner(dls, n_factors=50, y_range=(1,5))
    # Traings the model on the inputted data with these parameters
    learn.fit_one_cycle(5, 5e-3, wd=0.1)

    # Make predictions on the test data
    test_dls = CollabDataLoaders.from_df(test, bs=128)
    test_preds, _ = learn.get_preds(dl=test_dls.valid)
    # Compare our predicitons vs the actual ratings
    test_actuals = test_dls.valid.dataset.items['stars'].values 

    # RMSE formula
    rmse = np.sqrt(((test_preds.numpy() - test_actuals)**2).mean())

    warnings.resetwarnings()

    return rmse  

def grid_search(dls, n_factors_values, y_range_values, lr_values, wd_values, results, test, num_epochs=5):
    for n_factors, y_range, lr, wd in product(n_factors_values, y_range_values, lr_values, wd_values):
        # Create collab_learner with current hyperparameters
        learn = collab_learner(dls, n_factors=n_factors, y_range=y_range)

        learn.fit_one_cycle(num_epochs, lr, wd=wd)

        test_dls = CollabDataLoaders.from_df(test, bs=128)
        test_preds, _ = learn.get_preds(dl=test_dls.valid)  # Get only the predictions
        test_actuals = test_dls.valid.dataset.items['stars'].values  # Use valid dataset to get items

        rmse = np.sqrt(((test_preds.numpy() - test_actuals)**2).mean())

        results.append(f"n_factors={n_factors}, y_range={y_range}, lr={lr}, wd={wd} - RMSE: {rmse}")

def get_rmse(line):
    return float(line.split('- RMSE: ')[1])

def fastai_hyperparameter(data):

    warnings.filterwarnings("ignore", category=UserWarning, module="fastai.torch_core")

    train, test = train_test_split(data, test_size=0.2, random_state=42)

    # Creates the data loader for the collaborative filtering
    dls = CollabDataLoaders.from_df(train, bs=64)

    results = []

    n_factors_values = [50, 100]
    y_range_values = [(1, 5)]
    lr_values = [0.001, 0.005, 0.01]
    wd_values = [0.1, 0.01, 0.001]

    grid_search(dls, n_factors_values, y_range_values, lr_values, wd_values, results, test)

    # Sort the lines based on the RMSE values
    sorted_lines = sorted(results, key=get_rmse)

    return sorted_lines[0].split('- RMSE: ')[1]

    warnings.resetwarnings()