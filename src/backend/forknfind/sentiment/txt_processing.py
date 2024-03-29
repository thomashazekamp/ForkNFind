'''
This file contains the functions needed to normalize the data from its respective dataset. These are the following steps in the normalization process:
1. Convert emojis to text
2. Remove links
3. Remove hashtags
4. Make all text lowercase
5. Removing repeated characters
6. Removing punctuation repetitions
7. Replacing contractions with their expanded form

References:
- Perform Sentiment Analysis on Twitter data by combining Text Mining and NLP techniques, NLTK and Scikit-Learn
- by Benjamin Termonia
- provided by Udemy Business
'''
import re # Used for regex
import emoji # Used to convert emojis to text

import contractions # Used to expand contractions

import nltk
import ssl # Used to fix SSL error when downloading nltk data

'''
Error handling for nltk download and issue with SSL
Reference: https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed
    and https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087
'''
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.tokenize import word_tokenize
nltk.download('punkt')

import string
from nltk.corpus import stopwords
nltk.download('stopwords')

# Stemming
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer # more agressive stemming
from nltk.stem import SnowballStemmer # better than porter and newer

# Remove emojis
def convert_emoji_to_text(text):
    text = emoji.demojize(text) # Converting the emoji to their word meaning
    text = text.replace(":"," ") # Replacing the colon symbol with a space
    return text

# Remove links
def remove_links(text, replace_with=""):
    text = re.sub('(http|https):\/\/\S+', replace_with, text) # regex to remove any links starting with http or https
    return text

# Remove hashtags
def remove_hashtags(text, replace_with=""):
    text = re.sub('#+', replace_with, text) # regex to remove any hashtags
    return text


# Make all text lowercase
def lower_case_string(text):
    return text.lower()


# Removing repeated characters
def remove_letter_repetitions(text):
    return re.sub(r'(.)\1+', r'\1\1', text) # regex to remove repeated chars, firstly matches a char which is repeated more than once, then replaces it with the same char twice

# Removing punctuation repetitions
def remove_punctuation_repetitions(text, replace_with=""):
    return re.sub(r'[\?\.\!]+(?=[\?\.\!])', replace_with, text) # regex to remove repeated punctuation, firstly matches a punctuation which is repeated more than once, then replaces it with a single punctuation

'''
Replacing contractions with their expanded form
'''
# Replacing contractions with their full form: e.g I'm -> I am
def replace_contractions(text):
    text = contractions.fix(text) # Using built in method from contractions library
    return text

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

# Function to stem tokens given a stemming algorithm, e.g. porter, lancaster, snowball
def stemming_tokens(tokens, stemmer):
    # depending on the chosen stemmer, we will use the respective stemming algorithm
    if stemmer == 'porter':
        stemmer = PorterStemmer()
    elif stemmer == 'lancaster':
        stemmer = LancasterStemmer()
    elif stemmer == 'snowball':
        stemmer = SnowballStemmer('english')
    else:
        raise ValueError('Stemmer not recognized - please choose between porter, lancaster or snowball.')

    # Stemming the tokens using specified stemmer
    token_list = [stemmer.stem(token) for token in tokens] # Add the new stemmed token to the list
    return token_list

# Function to process the text, removing links, converting emojis to text, removing hashtags, making string lowercase, removing repeated characters and punctuation and replacing contractions
def process_text(text):
    # Removing links and converting emojis to text
    p_txt = remove_links(text)
    p_txt = convert_emoji_to_text(p_txt)

    # Removing hashtags, making string lowercase, removing repeated characters and punctuation and replacing contractions
    p_txt = remove_hashtags(p_txt)
    p_txt = lower_case_string(p_txt)
    p_txt = remove_letter_repetitions(p_txt)
    p_txt = remove_punctuation_repetitions(p_txt)
    p_txt = replace_contractions(p_txt)
    
    # Tokenizing the string
    p_txt = custom_tokenization(p_txt)

    # Stemming the tokens, using the snowball stemmer
    p_txt = stemming_tokens(p_txt, 'snowball')
    return p_txt