from keywords_data import *
from template_data import *
import re
import random

def detect_question_topic(user_input):
    """
    检测用户输入属于哪个问题主题分类（topic），根据 question_topic_keywords 中的短语进行匹配。
    """
    for topic, phrases in questions_topic_keywords.items():
        for phrase in phrases:
            # 精确匹配短语或作为子串存在
            pattern = re.escape(phrase.lower())
            if re.search(rf"\b{pattern}\b", user_input) or phrase in user_input:
                return topic
    return None


def handle_question_and_response(user_input, style, furhat):
    topic = detect_question_topic(user_input)
    key = (topic, style)  # style 保持小写即可

    # 使用模板查找
    response = template_questions.get(key)
    # 如果找不到对应的模板
    if response is None:
        if topic is None:
            response = (
                "Thanks for telling me that. Could you tell me a bit more about what you’re facing？ "
                "For example, is it about interviews, resume, or finding direction?"
            )
        else:
            response = (
                "I see you're asking about something important. I’m still learning to answer this better."
                "Would you like to talk more about it?"
            )

    if furhat:
        gesture = get_gesture_for_topic(topic)
        furhat.gesture(name=gesture)
    return response

def get_gesture_for_topic(topic):
    topic_gestures = {
        "interview_acquisition": ["Smile", "Nod"],
        "interview_preparation": ["Nod", "BrowRaise"],
        "interview_performance": ["BrowRaise", "Thoughtful"],
        "interview_adjustment": ["ExpressSad", "Nod"],
        "resume_writing": ["Nod", "Smile"],
        "resume_problems": ["Thoughtful", "ExpressSad"],
        "career_planning": ["Thoughtful"],
        "industry_choice": ["BrowRaise"],
        "job_matching": ["Thoughtful", "Smile"],
        "how_to_start": ["Nod", "Smile"],
        "platforms": ["Nod"],
        "job_strategy": ["BrowRaise", "Nod"]
    }

    gestures = topic_gestures.get(topic, ["Smile"])
    return random.choice(gestures)
