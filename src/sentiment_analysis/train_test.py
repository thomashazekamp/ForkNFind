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