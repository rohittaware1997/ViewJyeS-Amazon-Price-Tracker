import pika
import csv
import json
import ast
import warnings
# warnings.filterwarnings('ignore')
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


from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression

import Predict



def on_message_received (ch, method, properties, body):
    data1 = body.decode()
    reviews_list = ast.literal_eval(data1)
    with open('reviews.csv', mode='w', encoding="utf-8") as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Reviews','Sentiment'])
        # Write each string as a row in the CSV file, with an increasing index
        for review in (reviews_list):
            writer.writerow([review, 1])
    print("received new message", data1)
    Predict.predict()




connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='my_queue')

channel.basic_consume(queue='my_queue', auto_ack=True, on_message_callback=on_message_received)

print("Starting consuming")

channel.start_consuming()
print("received new message", result)