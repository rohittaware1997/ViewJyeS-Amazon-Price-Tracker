import pickle
import json
import pika
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import nltk
import ssl
from sklearn.metrics import accuracy_score

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression



def clean_review(review):
            stp_words = stopwords.words('english')
            clean_review = " ".join(word for word in review.split() if word not in stp_words)
            return clean_review


def predict():
            print("Entered")
            with open('my_model.pkl', 'rb') as file:
                model = pickle.load(file)

            data = pd.read_csv('Amazon_Reviews.csv')
            print("Original Shape:", data.shape)
            data.dropna(inplace=True)

            data.loc[data['Sentiment']<=3, 'Sentiment'] = 0
            data.loc[data['Sentiment']>3, 'Sentiment'] = 1

            data['Review'] = data['Review'].apply(clean_review)

                    # Vectorize training data
            cv = TfidfVectorizer()
            X_train = cv.fit_transform(data['Review']).toarray()
            y_train = data['Sentiment']

                    # Train logistic regression model

            test_data = pd.read_csv('reviews.csv')
            test_data.dropna(inplace=True)
            test_data['Reviews'] = test_data['Reviews'].apply(clean_review)

            # Vectorize test data
            X_test = cv.transform(test_data['Reviews']).toarray()

            # Make predictions
            pred = model.predict(X_test)
            print(pred)
            pos, neg = get_percentage(pred)
            final_ans = [pos, neg]
            message = json.dumps(final_ans)
            print(message)
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            channel.queue_declare(queue='output_queue')

            channel.basic_publish(exchange='',
                        routing_key='output_queue',
                                               body=message)

            connection.close()


def get_percentage(pred):
    num_zeros = len(pred[pred == 0])
    num_ones = len(pred[pred == 1])
    total = num_zeros + num_ones
    percent_zeros = round(num_zeros/total * 100, 2)
    percent_ones = round(num_ones/total * 100, 2)
    print(percent_zeros, percent_ones)
    return percent_zeros, percent_ones