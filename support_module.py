from keywords_data import *
from template_data import *
import re
import random

def detect_topic(user_input):
    """
    检测用户输入的主要主题，从topic_keywords中匹配。
    """
    for topic, keywords in topic_keywords.items():
        for word in keywords:
            if word in user_input.lower():
                return topic
    return None

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

def get_subtopics_for_topic(main_topic):
    """获取主题对应的子主题列表"""
    subtopics = []
    if main_topic == "interview":
        return [topic for topic in questions_topic_keywords.keys() if topic.startswith("interview_")]
    elif main_topic == "resume":
        return [topic for topic in questions_topic_keywords.keys() if topic.startswith("resume_")]
    elif main_topic == "job_type":
        return ["career_planning", "industry_choice", "job_matching"]
    elif main_topic == "no_start_point":
        return ["how_to_start", "platforms", "job_strategy"]
    return subtopics


def get_clean_subtopic_name(subtopic):
    """完全清除子主题中的所有前缀，返回纯净的子主题名称"""
    # 移除所有前缀
    clean_name = subtopic
    prefixes = ["interview_", "resume_", "career_", "job_", "industry_"]
    for prefix in prefixes:
        clean_name = clean_name.replace(prefix, "")

    # 将下划线替换为空格
    clean_name = clean_name.replace("_", " ")
    return clean_name


def handle_question_and_response(user_input, style, furhat):
    # 先检测特定问题主题
    topic = detect_question_topic(user_input)
    key = (topic, style)

    # 使用模板查找
    response = template_questions.get(key)

    # 如果找不到对应的模板
    if response is None:
        if topic is None:
            # 没有识别到具体问题主题，检查是否有主要主题
            main_topic = detect_topic(user_input)

            if main_topic:
                # 识别到主题但没有具体问题，列出相关子主题
                subtopics = get_subtopics_for_topic(main_topic)

                if subtopics:
                    # 有子主题，根据风格提供不同提示
                    if style == "warm":
                        readable_topic = main_topic.replace("_", " ")
                        readable_subtopics = []

                        for subtopic in subtopics:
                            # 完全清除前缀，获取纯净的子主题名称
                            clean_subtopic = get_clean_subtopic_name(subtopic)
                            readable_subtopics.append(clean_subtopic)

                        subtopics_text = ", ".join(readable_subtopics[:-1])
                        if len(readable_subtopics) > 1:
                            subtopics_text += f", or {readable_subtopics[-1]}"
                        else:
                            subtopics_text = readable_subtopics[0]

                        response = (f"I see you're interested in {readable_topic}. I'd love to help more specifically! "
                                    f"Could you tell me if it's about {subtopics_text}?")
                    else:  # neutral style
                        readable_topic = main_topic.replace("_", " ")
                        readable_subtopics = []

                        for subtopic in subtopics:
                            # 完全清除前缀，获取纯净的子主题名称
                            clean_subtopic = get_clean_subtopic_name(subtopic)
                            readable_subtopics.append(clean_subtopic)

                        subtopics_formatted = " | ".join(readable_subtopics)
                        response = (
                            f"Topic: {readable_topic}. Specify subtopic for detailed assistance: {subtopics_formatted}")
                else:
                    # 没有子主题的兜底
                    if style == "warm":
                        response = (f"Thanks for sharing about your {main_topic.replace('_', ' ')}. "
                                    f"Could you tell me more specifically what you'd like help with?")
                    else:
                        response = (f"Topic identified: {main_topic.replace('_', ' ')}. "
                                    f"Please provide more specific details about your requirements.")
            else:
                # 没有识别到任何主题的兜底 - 修改为使用指定的举例文本
                if style == "warm":
                    response = (
                        "Thanks for telling me that. Could you tell me a bit more about what you're facing? "
                        "For example, is it about interview, resume, job type, or finding a start point?"
                    )
                else:
                    response = (
                        "Input received. Please specify your primary concern: interview, resume, job type, or finding a start point."
                    )
        else:
            # 识别到子主题但没有模板的兜底
            if style == "warm":
                # 完全清除前缀，获取纯净的子主题名称
                clean_topic = get_clean_subtopic_name(topic)
                response = (
                    f"I see you're asking about {clean_topic}. I'd love to help with that. "
                    f"Could you tell me more about what specific aspect you're interested in?"
                )
            else:
                # 完全清除前缀，获取纯净的子主题名称
                clean_topic = get_clean_subtopic_name(topic)
                response = (
                    f"Topic identified: {clean_topic}. "
                    f"Additional details required for comprehensive assistance."
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