import nltk
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

"""
The code in this class is originated from https://www.kaggle.com/code/alvations/basic-nlp-with-nltk
It is used to convert the words into their root word with linguistics rules (with the use of regexes)
"""
class Lemmatization:

    @staticmethod
    def penn2morphy(penntag):
        """ Converts Penn Treebank tags to WordNet. """
        morphy_tag = {'NN': 'n', 'JJ': 'a',
                      'VB': 'v', 'RB': 'r'}
        try:
            return morphy_tag[penntag[:2]]
        except:
            return 'n'

    @staticmethod
    def lemmatize_sent(text):
        wnl = WordNetLemmatizer()
        # Text input is string, returns lowercased strings.
        return ' '.join([wnl.lemmatize(word, pos=Lemmatization.penn2morphy(tag))
                         for word, tag in pos_tag(word_tokenize(text))])
