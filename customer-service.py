import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('subjectivity')
nltk.download('movie_reviews')

analyzer= SentimentIntensityAnalyzer()

while True:
    next_message = input("Message: ")
    scores= analyzer.polarity_scores(next_message)
    compound= scores["compound"]
    if compound > 0.1:
        print("Positive")
    elif compound <-0.1:
        print("Negative")
    else:
        print("Neutral")