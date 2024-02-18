'''
References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

import string
from nltk.corpus import stopwords
nltk.download('stopwords')

# Stemming
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer # more agressive stemming
from nltk.stem import SnowballStemmer # better than porter and newer
#NOTE: can look at more stemming algos


# def tokenize(text): # Tokenizing the text
#     tokens = word_tokenize(text)
#     return tokens

# Depending if we want to keep punctuation, alphanumeric characters and stopwords we can use the following function with True or False
def custom_tokenization(text, keep_punctuation = False, keep_alphanum = False, keep_stopwords = False):
    stop_words = set(stopwords.words('english')) # Getting the stop words from nltk
    token_list = word_tokenize(text)

    if not keep_punctuation:
        token_list = [token for token in token_list if token not in string.punctuation] # Add only if not in the punctuation list
    if not keep_alphanum:
        token_list = [token for token in token_list if token.isalpha()] # Add only if is a letter
    if not keep_stopwords:
        stop_words = set(stopwords.words('english'))
        stop_words.discard('not') # Remove stop words which are relevant for sentiment analysis from the stop words list !NOTE: Can add more words to be excluded
        token_list = [token for token in token_list if token not in stop_words] # Add only if not in the stop words list

    return token_list

# Function to stem tokens given a stemming algorithm !NOTE: Need to change logic of which stemmer to use
def stemming_tokens(tokens, stemmer):
    porter_stemmer = PorterStemmer()
    lancaster_stemmer = LancasterStemmer()
    snowball_stemmer = SnowballStemmer('english')
    stemmer = snowball_stemmer # !!!NOTE: This needs to change logic
    token_list = [stemmer.stem(token) for token in tokens] # Add the new stemmed token to the list
    return token_list