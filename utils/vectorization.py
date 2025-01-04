import time
from sklearn.feature_extraction.text import TfidfVectorizer


class Vectorization:
    @staticmethod
    def apply_vectorization(text, vectorizer):
        start_time = time.time()
        vectorized_text = vectorizer.fit_transform(text)
        execution_time = time.time() - start_time
        return execution_time, vectorized_text

    @staticmethod
    def apply_tfidf(texts):
        vectorizer = TfidfVectorizer()
        return Vectorization.apply_vectorization(texts, vectorizer)
