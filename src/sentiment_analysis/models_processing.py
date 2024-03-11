'''
References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''

'''
### Used ChatGPT to fix issue with relating to lambda function inside CountVectorizer and TfidfVectorizer
- Prompt: 
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sklearn/feature_extraction/text.py:525: UserWarning: The parameter 'token_pattern' will not be used since 'tokenizer' is not None'
  warnings.warn(
Traceback (most recent call last):
  File "/Users/thomashazekamp/Desktop/CASE4/CA400/2024-ca400-hazekat2-dalye54/src/sentiment_analysis/runner_sent_analysis.py", line 59, in <module>
    main()
  File "/Users/thomashazekamp/Desktop/CASE4/CA400/2024-ca400-hazekat2-dalye54/src/sentiment_analysis/runner_sent_analysis.py", line 56, in main
    print(predict_sentiment(example_text))
  File "/Users/thomashazekamp/Desktop/CASE4/CA400/2024-ca400-hazekat2-dalye54/src/sentiment_analysis/runner_sent_analysis.py", line 34, in predict_sentiment
    dump((model, text_trans), model_file_name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/joblib/numpy_pickle.py", line 553, in dump
    NumpyPickler(f, protocol=protocol).dump(value)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 487, in dump
    self.save(obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/joblib/numpy_pickle.py", line 355, in save
    return Pickler.save(self, obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 560, in save
    f(self, obj)  # Call unbound method with explicit self
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 886, in save_tuple
    save(element)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/joblib/numpy_pickle.py", line 355, in save
    return Pickler.save(self, obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 603, in save
    self.save_reduce(obj=obj, *rv)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 717, in save_reduce
    save(state)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/joblib/numpy_pickle.py", line 355, in save
    return Pickler.save(self, obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 560, in save
    f(self, obj)  # Call unbound method with explicit self
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 971, in save_dict
    self._batch_setitems(obj.items())
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 997, in _batch_setitems
    save(v)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/joblib/numpy_pickle.py", line 355, in save
    return Pickler.save(self, obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 560, in save
    f(self, obj)  # Call unbound method with explicit self
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pickle.py", line 1070, in save_global
    raise PicklingError(
_pickle.PicklingError: Can't pickle <function run_model.<locals>.fit_tfidf.<locals>.<lambda> at 0x7fe7b9e77280>: it's not found as models_processing.run_model.<locals>.fit_tfidf.<locals>.<lambda>

- Solution:
The error you encountered indicates that there is a problem with pickling (serializing) a lambda function defined inside your run_model function. Lambda functions can sometimes cause issues with serialization due to their nature.

To resolve this issue, you can try avoiding the use of lambda functions within your run_model function. Instead, you can define named functions or use built-in functions. Once you've done that, try saving your model and text transformer again.

If you continue to encounter issues, please provide more details about your run_model function, particularly any parts involving lambda functions or custom objects that might not be picklable. This will help in providing more specific guidance on how to address the problem.

### Other helpful resources:
- https://github.com/joblib/joblib/issues/600

### Reference for the models being used:
- https://www.linkedin.com/advice/0/what-nlp-models-most-effective-sentiment-dbtef#:~:text=Supervised%20machine%20learning%20models%2C%20such,neutral%2C%20based%20on%20labeled%20examples.
- Notes by Vikram Pandya
'''
## Libraries used
# Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

## Functions
def custom_preprocessor(text):
    return text

def custom_tokenizer(text):
    return text

# Adding text vectorization, including the use of model
# Uses tfidf as default
def run_model(vectorization_type, model_type):

    from runner_sent_analysis import process_data # calling the process_data function from the runner_sent_analysis file

    print(f'Running {model_type} model...')
    print('Vectorization type:', vectorization_type)

    x, y = process_data() # calls process data with x and y being the text tokens and sentiment of the text
    corpus = x # corpus is the text tokens of whole dataset

    # BAG OF WORDS (CountVectorizer)
    def fit_cv(text_corpus):
        cv_vect = CountVectorizer(tokenizer=custom_tokenizer, preprocessor=custom_preprocessor) # Using custom tokenizer and preprocessor

        cv_vect.fit(text_corpus)

        return cv_vect
    
    # TF-IDF (TfidfVectorizer)
    def fit_tfidf(text_corpus):
        tf_vect = TfidfVectorizer(preprocessor=custom_preprocessor, tokenizer=custom_tokenizer) # Using custom tokenizer and preprocessor

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


    ### Fitting the model

    # Logistic Regression model
    def fit_lr(x_train, y_train): # Fitting a logistic regression model
        lr = LogisticRegression()
        lr.fit(x_train, y_train)
        return lr
    
    # Naive Bayes model
    def fit_nb(x_train, y_train):
        nb = MultinomialNB()
        nb.fit(x_train, y_train)
        return nb
    
    # Support Vector Machine model
    def fit_svm(x_train, y_train):
        svm = SVC()
        svm.fit(x_train, y_train)
        return svm
    
    # Random Forest model
    def fit_rf(x_train, y_train):
        rf = RandomForestClassifier()
        rf.fit(x_train, y_train)
        return rf
    
    # Gradient Boosting Machine model
    def fit_gbm(x_train, y_train):
        gbm = GradientBoostingClassifier()
        gbm.fit(x_train, y_train)
        return gbm


    ### Vectorization
    # Bag of Words (CountVectorizer)
    if vectorization_type == 'cv':
        cv = fit_cv(x_train) # only fit on the training data
        x_train_cv = cv.transform(x_train) # transform the training data
        x_test_cv = cv.transform(x_test) # transform the testing data

        if model_type == 'logistic_regression': # if the model type is logistic regression
            model_cv = fit_lr(x_train_cv, y_train) # fit the model on the training data

        elif model_type == 'naive_bayes': # if the model type is naive bayes
            model_cv = fit_nb(x_train_cv, y_train)

        elif model_type == 'support_vector_machine': # if the model type is support vector machine
            model_cv = fit_svm(x_train_cv, y_train)

        elif model_type == 'random_forest': # if the model type is random forest
            model_cv = fit_rf(x_train_cv, y_train)

        elif model_type == 'gradient_boosting_machine':     
            model_cv = fit_gbm(x_train_cv, y_train)
        else:
            exit("Model provided is INVALID. Please use one of the following:\n'logistic_regression', 'naive_bayes', 'support_vector_machine', 'random_forest', 'gradient_boosting_machine'")

        return model_cv, cv # return the model and the count vectorizer


    # Using TF-IDF
    elif vectorization_type == 'tfidf':
        tf = fit_tfidf(x_train) # only fit on the training data
        x_train_tf = tf.transform(x_train) # transform the training data
        x_test_tf = tf.transform(x_test) # transform the testing data

        if model_type == 'logistic_regression': # if the model type is logistic regression
            model_tf = fit_lr(x_train_tf, y_train) # fit the model on the training data

        elif model_type == 'naive_bayes': # if the model type is naive bayes
            model_tf = fit_nb(x_train_tf, y_train)

        elif model_type == 'support_vector_machine': # if the model type is support vector machine
            model_tf = fit_svm(x_train_tf, y_train)

        elif model_type == 'random_forest': # if the model type is random forest
            model_tf = fit_rf(x_train_tf, y_train)

        elif model_type == 'gradient_boosting_machine':     
            model_tf = fit_gbm(x_train_tf, y_train)
        else:
            exit("Model provided is INVALID. Please use one of the following:\n'logistic_regression', 'naive_bayes', 'support_vector_machine', 'random_forest', 'gradient_boosting_machine")

        return model_tf, tf # return the model and the tfidf vectorizer