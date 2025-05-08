# dialogue_manager.py
from emotion_recognition import get_user_emotion
import random


def apply_state_gesture(furhat, state):
    positive_gestures = ["BigSmile", "Smile", "Nod", "BrowRaise"]
    negative_gestures = ["BrowFrown", "ExpressSad", "ExpressFear", "Thoughtful"]

    if state == "comfort":
        gesture = random.choice(negative_gestures)
    elif state == "support":
        gesture = random.choice(positive_gestures)
    else:
        print(f"[Warning] Unknown state: {state}, no gesture applied.")
        return

    print(f"[Gesture] Applying gesture '{gesture}' for state '{state}'")
    furhat.gesture(name=gesture)

def chatbot_response(user_input, style):
    """
    调用 blenderbot 生成回应，根据 style 拼接指令
    :param user_input: 用户输入
    :param style: 当前风格 ('warm' or 'neutral')
    :return: 模型生成的回应
    """
    print(style)
    if style == "warm":
        print("start warm style")
        prompt = "You are a warm, empathetic coach. Respond kindly to: " + user_input
    else:
        print("start neutral style")
        prompt = "You are a neutral, professional coach. Respond objectively to: " + user_input

    inputs = tokenizer(prompt, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return response

class DialogueManager:
    def __init__(self):
        self.current_style = "neutral"  # 默认“中立”风格
        self.session_state = "comfort"  # 默认“心理疏导”
        print(f"[Init] Current style: {self.current_style}, Initial state: {self.session_state}")

    def parse_style_command(self, user_input):
        """识别用户输入中是否有切换风格指令"""
        if "warm" in user_input:
            return "warm"
        elif "neutral" in user_input:
            return "neutral"
        return None

    def update_style(self, new_style):
        """更新风格"""
        if new_style and new_style != self.current_style:
            self.current_style = new_style
            return f"Switched to {new_style} mode."
        elif new_style == self.current_style:
            return f"Already in {new_style} mode."
        return None

    def detect_emotion_and_update_state(self, user_input):
        """这里假设情绪分析函数返回固定值 → 你可以替换实际函数"""
        polarity = get_user_emotion(user_input)
        print(f"[Emotion] Detected polarity: {polarity}")
        if polarity >= 0:
            self.session_state = "support"
        else:
            self.session_state = "comfort"
        print(f"[State Update] Current state: {self.session_state}")


    def generate_response(self, user_input):
        """综合处理用户输入 → 返回 chatbot 生成的回应"""

        self.detect_emotion_and_update_state(user_input)

        if self.session_state == "comfort":
            user_prompt = "The user needs comfort: " + user_input
        else:
            user_prompt = "The user needs job support: " + user_input


        return chatbot_response(user_prompt, self.current_style)






