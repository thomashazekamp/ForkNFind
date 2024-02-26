from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
import random
from sklearn.linear_model import LogisticRegression

# Adding text vectorization, including the use of model
def run_model():

    from runner_sent_analysis import process_data # calling the process_data function from the runner_sent_analysis file
    x, y = process_data()
    corpus = x

    # Bag of words and TF-IDF can be kept in here / or the train/test can be moved in here as they are related and used together
    # BAG OF WORDS (CountVectorizer)
    # from sklearn.feature_extraction.text import CountVectorizer # added at top of file

    # def fit_cv(tweet_corpus):
    #     cv_vect = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x) # Using custom tokenizer and preprocessor

    #     cv_vect.fit(tweet_corpus)

    #     return cv_vect

    # cv_vect = fit_cv(corpus)

    # ft = cv_vect.get_feature_names_out()


    # cv_mtx = cv_vect.transform(corpus)

    ### TF-IDF (TfidfVectorizer)

    # from sklearn.feature_extraction.text import TfidfVectorizer - added at top of file

    def fit_tfidf(tween_corpus):
        tf_vect = TfidfVectorizer(preprocessor=lambda x: x, tokenizer=lambda x: x) # Using custom tokenizer and preprocessor

        tf_vect.fit(tween_corpus)
        return tf_vect

    tf_vect = fit_tfidf(corpus)
    tf_mtx = tf_vect.transform(corpus)

    # from sklearn.model_selection import train_test_split
    # import random - added both at top of file

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.8)

    # Logistic Regression model
    # from sklearn.linear_model import LogisticRegression - added at top of file

    def fit_lr(x_train, y_train): # Fitting a logistic regression model
        lr = LogisticRegression()
        lr.fit(x_train, y_train)
        return lr

    # Using bag of words
    # cv = fit_cv(x_train) # only fit on the training data
    # x_train_cv = cv.transform(x_train) # transform the training data
    # x_test_cv = cv.transform(x_test) # transform the testing data


    # model_lr_cv = fit_lr(x_train_cv, y_train) # fit the model on the training data

    # return model_lr_cv, cv


    ### Using TF-IDF
    tf = fit_tfidf(x_train) # only fit on the training data
    x_train_tf = tf.transform(x_train) # transform the training data
    x_test_tf = tf.transform(x_test) # transform the testing data

    model_lr_tf = fit_lr(x_train_tf, y_train) # fit the model on the training data

    return model_lr_tf, tf