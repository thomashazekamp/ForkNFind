from sklearn.model_selection import train_test_split
from fastai.tabular.all import *
from fastai.collab import *
import warnings


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
