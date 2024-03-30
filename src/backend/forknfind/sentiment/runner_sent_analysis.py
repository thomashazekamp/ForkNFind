'''
This file is the runner file that will call all the necessary functions to run the sentiment analysis model
References:
- https://neptune.ai/blog/saving-trained-model-in-python -> used for saving the model (joblib)
'''
# Using necessary functions from other files
from .models_processing import run_model
from .txt_processing import process_text

# Importing necessary libraries
from joblib import dump, load
from datetime import datetime
import os
import pickle


# Predict the sentiment of a given text
def predict_sentiment(text, vectorization_type='tfidf', model_type='support_vector_machine'):
    # Print the current time
    #print(f'Current time at start: {datetime.now()}')

    # File name depending on the model and vectorization type with the path
    model_file_name = 'forknfind/sentiment/saved_models_pkl/sentiment_analysis_model_' + vectorization_type + '_' + model_type + '.pkl'

    # var to establish forcefully running the model
    run_save_model = False # Last updated: 12/3

    if os.path.isfile(model_file_name) and (run_save_model == False): # if the file exists and we dont want to run the model (run_save_model = False), then load the already saved model)
        # Load saved model with error handling
        try:
            model, text_trans = load(model_file_name) # load the model and text transformer
        except FileNotFoundError:
            print("Model file not found. Please initially run the model to save it.")
    else:
        model, text_trans = run_model(vectorization_type, model_type) # returns the model and the text transformer, can have input such as: 'cv' or 'tfidf' (uses tfidf as default option) to choose which vectorization type to use
        # Save the model and text transformer to a file
        dump((model, text_trans), model_file_name)


    processed_text = process_text(text) # process the text - remove links, convert emojis to text, remove hashtags, make string lowercase, remove repeated characters and punctuation and replace contractions
    new_text = text_trans.transform([processed_text]) # transform the processed text - using the text transformer
    prediction = model.predict(new_text) # predict the sentiment of the new text - using the model

    #print(f'Current time at end: {datetime.now()}')

    # Checking if the prediction is positive or negative with an error case
    if prediction == 1:
        return '1'  # positive sentiment
    elif prediction == 0:
        return '0'  # negative sentiment
    else:
        return 'NA - error'  # not available / error

def run():
    '''
    Documentation:
    - When calling predict_sentiment
        - first parameter requires the text to be analyzed
        - second parameter requires the vectorization type (if none provided, uses 'tfidf' as default) - 'cv' or 'tfidf'
        - third parameter requires the model type (if none provided, uses 'logistic_regression' as default) - 'logistic_regression', 'random_forest', 'naive_bayes', 'support_vector_machine', 'gradient_boosting_machine'
    note: if a third parameter is provided, the second parameter must also be provided
    '''
    # This can be used for example purposes
    example_text = "I am happy, this is great!"
    example_text2 = "I am sad, this is terrible!"
    print(predict_sentiment(example_text2))
