import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('stopwords')

class Utilities:

    @staticmethod
    def remove_stopwords(text):
        # tokenize the text
        words = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        # remove punctuation and stop words
        filtered_words = [word for word in words if word not in stop_words and word not in string.punctuation]
        # filtered_words = [word for word in words if word not in stop_words]

        # join the filtered words back into a string
        return " ".join(filtered_words)

    # some punctuation (like '...')  is not removed with the above function
    # therefore we also use this to remove them
    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    """
    Removes html elements from text (e.g <br>)
    """
    @staticmethod
    def remove_html(text):
        beautiful_soup = BeautifulSoup(text, 'html.parser')
        return beautiful_soup.get_text()

    """
    The final method to preprocess text. It converts all letters to lower case and removes stop words and punctuations
    """
    @staticmethod
    def preprocess(text):
        temp_text = text.lower()  # convert all letters to lower case
        temp_text = Utilities.remove_stopwords(temp_text)  # remove stop words
        return Utilities.remove_punctuation(temp_text)
