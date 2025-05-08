from textblob import TextBlob
from template_data import *
from keywords_data import *
import random

def get_user_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

def get_emotion_category(text):
    for category, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in text.lower():
                return category
    return "unknown"


def detect_topic(user_input):
    """
    Detects potential user topic from keywords.
    Returns one of: 'resume', 'interview', 'career_direction', 'anxiety', or None
    """

    for topic, keywords in topic_keywords.items():
        for word in keywords:
            if word in user_input:
                return topic
    return None


def handle_emotion_and_topic(user_input, style, furhat):
    emotion = get_emotion_category(user_input)
    topic = detect_topic(user_input)
    key = (emotion, topic, style)  # style 保持小写即可

    # 使用模板查找
    response = template_emotions.get(key)

    # 如果找不到，尝试降级到“仅情绪”类
    if response is None:
        key = (emotion, None, style)
        response = template_emotions.get(key)

    # 如果还找不到，使用兜底默认回应
    if response is None:
        if style == "warm":
            response = "Thank you so much for sharing that with me. I'm here to support you through your job search journey. For example, would you like to talk about interviews, resume, or finding direction? I'm here to listen and help."
        else: #netrual style
            response = "Input received. For productive assistance, please specify your job search concern. Available topics: interviews, resume, or finding direction. What specific area requires assistance?"
    if furhat:
        positive_gestures = ["BigSmile", "Smile", "Nod", "BrowRaise"]
        negative_gestures = ["BrowFrown", "ExpressSad", "ExpressFear", "Thoughtful"]

        if emotion == "positive":
            furhat.gesture(name=random.choice(positive_gestures))
        else:
            furhat.gesture(name=random.choice(negative_gestures))

    return response

