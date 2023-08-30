import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
import ssl
from sklearn.metrics import accuracy_score
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
import pickle



def temp():
        def clean_review(review):
            stp_words = stopwords.words('english')
            clean_review = " ".join(word for word in review.split() if word not in stp_words)
            return clean_review

        # Load and preprocess training data
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
        model = LogisticRegression()
        model.fit(X_train, y_train)

        with open('my_model.pkl', 'wb') as file:
            pickle.dump(model, file)
        ################## write your code ####################
        # Load and preprocess test data
#         test_data = pd.read_csv('reviews.csv')
#         test_data.dropna(inplace=True)
#         test_data['Reviews'] = test_data['Reviews'].apply(clean_review)
#         print("test_data Shape:", data.shape)
#         # Vectorize test data
#         X_test = cv.transform(test_data['Reviews']).toarray()
#         print("X_test Shape:", data.shape)
#         # Make predictions
#         pred = model.predict(X_test)
#         print(pred)


temp()