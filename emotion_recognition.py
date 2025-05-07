from textblob import TextBlob


def get_user_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity