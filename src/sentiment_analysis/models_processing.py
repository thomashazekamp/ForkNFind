# Adding text vectorization, including the use of model

# Applying text processing to the data
# !!! Need to implement file calling for the functions (this needs to use the file that contains the dataset data)
# !! - read_dataset?
# Add the below to the file that contains the dataset data / maybe have it in a separate func that then does the .apply needed
# df["tokens"] = df["tweet_text"].apply(process_text)
# df["tweet_sentiment"] = df["sentiment"].apply(lambda x: 1 if x == "positive" else 0)

x  = df["tokens"].tolist()
y = df["tweet_sentiment"].tolist()

# Bag of words and TF-IDF can be kept in here / or the train/test can be moved in here as they are related and used together
# BAG OF WORDS (CountVectorizer)
from sklearn.feature_extraction.text import CountVectorizer # Bag of words

def fit_cv(tweet_corpus):
    cv_vect = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x) # Using custom tokenizer and preprocessor

    cv_vect.fit(tweet_corpus)

    return cv_vect

cv_vect = fit_cv(corpus)

ft = cv_vect.get_feature_names_out()


cv_mtx = cv_vect.transform(corpus)

# TF-IDF (TfidfVectorizer)

from sklearn.feature_extraction.text import TfidfVectorizer

def fit_tfidf(tween_corpus):
    tf_vect = TfidfVectorizer(preprocessor=lambda x: x, tokenizer=lambda x: x) # Using custom tokenizer and preprocessor

    tf_vect.fit(tween_corpus)
    return tf_vect

tf_vect = fit_tfidf(corpus)
tf_mtx = tf_vect.transform(corpus)

from sklearn.model_selection import train_test_split
import random

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.8)

# Logistic Regression model
from sklearn.linear_model import LogisticRegression

def fit_lr(x_train, y_train): # Fitting a logistic regression model
    lr = LogisticRegression()
    lr.fit(x_train, y_train)
    return lr

# Using bag of words
cv = fit_cv(x_train) # only fit on the training data
x_train_cv = cv.transform(x_train) # transform the training data
x_test_cv = cv.transform(x_test) # transform the testing data


model_lr_cv = fit_lr(x_train_cv, y_train) # fit the model on the training data


# Using TF-IDF
tf = fit_tfidf(x_train) # only fit on the training data
x_train_tf = tf.transform(x_train) # transform the training data
x_test_tf = tf.transform(x_test) # transform the testing data

model_lr_tf = fit_lr(x_train_tf, y_train) # fit the model on the training data