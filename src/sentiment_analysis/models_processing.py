'''
References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
import random
from sklearn.linear_model import LogisticRegression

# Adding text vectorization, including the use of model
# Uses tfidf as default
def run_model(vectorization_type):

    from runner_sent_analysis import process_data # calling the process_data function from the runner_sent_analysis file

    print('Running model...')
    print('Vectorization type:', vectorization_type)

    x, y = process_data() # calls process data with x and y being the text tokens and sentiment of the text
    corpus = x # corpus is the text tokens of whole dataset

    # BAG OF WORDS (CountVectorizer)
    def fit_cv(text_corpus):
        cv_vect = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x) # Using custom tokenizer and preprocessor

        cv_vect.fit(text_corpus)

        return cv_vect
    
    # TF-IDF (TfidfVectorizer)
    def fit_tfidf(text_corpus):
        tf_vect = TfidfVectorizer(preprocessor=lambda x: x, tokenizer=lambda x: x) # Using custom tokenizer and preprocessor

        tf_vect.fit(text_corpus) # fit the vectorizer on the corpus
        return tf_vect
    
    ### Vectorization
    # Bag of Words (CountVectorizer)
    if vectorization_type == 'cv':

        cv_vect = fit_cv(corpus)
        ft = cv_vect.get_feature_names_out()
        cv_mtx = cv_vect.transform(corpus)

    # TF-IDF (TfidfVectorizer)
    elif vectorization_type == 'tfidf':

        tf_vect = fit_tfidf(corpus) # calling the fit_tfidf function with the corpus
        tf_mtx = tf_vect.transform(corpus) # transforming the corpus using the tfidf vectorizer

    # error handling
    else:
        exit("Invalid vectorization type. Please use 'cv' or 'tfidf' as vectorization type. Changeable in runner_sent_analysis.py file, run_model called function.")


    ### Splitting data for train / test purposes
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.8)


    ### Logistic Regression model
    def fit_lr(x_train, y_train): # Fitting a logistic regression model
        lr = LogisticRegression()
        lr.fit(x_train, y_train)
        return lr

    ### Vectorization
    # Bag of Words (CountVectorizer)
    if vectorization_type == 'cv':
        cv = fit_cv(x_train) # only fit on the training data
        x_train_cv = cv.transform(x_train) # transform the training data
        x_test_cv = cv.transform(x_test) # transform the testing data


        model_lr_cv = fit_lr(x_train_cv, y_train) # fit the model on the training data

        return model_lr_cv, cv # return the model and the count vectorizer


    # Using TF-IDF
    elif vectorization_type == 'tfidf':
        tf = fit_tfidf(x_train) # only fit on the training data
        x_train_tf = tf.transform(x_train) # transform the training data
        x_test_tf = tf.transform(x_test) # transform the testing data

        model_lr_tf = fit_lr(x_train_tf, y_train) # fit the model on the training data

        return model_lr_tf, tf # return the model and the tfidf vectorizer