'''
This file is the runner file that will call all the necessary functions to run the sentiment analysis model
'''
# Using necessary functions from other files
from dataset_worker import read_dataset, apply_dataset_column_modifications, dataset_tolist
from models_processing import run_model
from txt_processing import process_text

# Importing necessary libraries
from joblib import dump, load

# Process the data by calling all relative dataset processing functions
def process_data():
    # Read dataset
    df = read_dataset()

    # Apply text processing and modifications to the dataset
    df = apply_dataset_column_modifications(df)

    # Convert the dataset to lists
    x, y = dataset_tolist(df) # holds the x = tokens and y = text_sentiment

    return x, y

# Predict the sentiment of a given text
def predict_sentiment(text, vectorization_type='tfidf'):
    run_save_model = True
    model_file_name = 'sentiment_analysis_model.pkl'

    if run_save_model == True:
        model, text_trans = run_model(vectorization_type) # returns the model and the text transformer, can have input such as: 'cv' or 'tfidf' (uses tfidf as default option) to choose which vectorization type to use

        # Save the model and text transformer
        dump((model, text_trans), model_file_name)

    try:
        model, text_trans = load(model_file_name) # load the model and text transformer
    except FileNotFoundError:
        print("Model file not found. Please initially run the model to save it.")

    processed_text = process_text(text) # process the text - remove links, convert emojis to text, remove hashtags, make string lowercase, remove repeated characters and punctuation and replace contractions
    new_text = text_trans.transform([processed_text]) # transform the processed text - using the text transformer
    prediction = model.predict(new_text) # predict the sentiment of the new text - using the model

    # Checking if the prediction is positive or negative with an error case
    if prediction == 1:
        return '1'  # positive sentiment
    elif prediction == 0:
        return '0'  # negative sentiment
    else:
        return 'NA'  # not available / error

def main():
    # This can be used for example purposes
    example_text = "I am happy, this is great!"
    example_text2 = "I am sad, this is terrible!"
    print(predict_sentiment(example_text2))

if __name__ == '__main__':
    main()