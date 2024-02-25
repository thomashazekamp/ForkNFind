'''
This file is the runner file that will call all the necessary functions to run the sentiment analysis model
'''
from dataset_worker import read_dataset, apply_dataset_column_modifications, dataset_tolist
from models_processing import run_model
from txt_processing import process_text

def process_data():
    # Read dataset
    df = read_dataset()

    # Apply text processing and modifications to the dataset
    df = apply_dataset_column_modifications(df)

    x, y = dataset_tolist(df) # holds the x = tokens and y = tweet_sentiment

    return x, y

# # Read dataset
# df = read_dataset()

# # Apply text processing and modifications to the dataset
# df = apply_dataset_column_modifications(df)

# x, y = dataset_tolist(df) # holds the x = tokens and y = tweet_sentiment

def main():
    # print(df.head())
    # print(x)
    # print(y)
    example_text = "I am happy"

    model, text = run_model() # returns the model and the text

    processed_text = process_text(example_text)
    new_text = text.transform([processed_text])
    prediction = model.predict(new_text)

    print(prediction)
    if prediction == 1:
        print("The text is positive")
    else:
        print("The text is negative")
    pass

if __name__ == '__main__':
    main()
