# main.py
# main.py
from furhat_remote_api import FurhatRemoteAPI
from dialogue_manager import *
import time
from emotion_recognition import *
from support_module import *
from log_redirect import *

start_logging()

# 连接 Furhat
furhat = FurhatRemoteAPI("localhost")  # 替换成你的 Furhat IP


# 设置 mask、voice、gesture
furhat.set_voice(name="Ruth-Neural")
furhat.set_led(red=0, green=0, blue=255)  # 可选：设置眼睛颜色为蓝色
furhat.set_face(character="anonymous", mask="anime[legacy]")
furhat.gesture(name="BigSmile")
dm = DialogueManager()

# 欢迎语
print(f"[Robot]: Hello! I'm WellPath！Before we start, do you prefer a warm tone or a neutral tone?")
furhat.say(text="Hello! I'm WellPath！Before we start, do you prefer a warm tone or a neutral tone?", blocking=True)

# 监听用户选择风格
while True:
    result = furhat.listen()
    # if not result or not result.message:
    #     furhat.say(text="Sorry, I didn't catch that. Could you repeat?", blocking=True)
    #     continue

    user_input = result.message.lower()
    print(f"[User]: {user_input}")

    # 尝试切换风格
    style_command = dm.parse_style_command(user_input)
    if style_command:
        dm.update_style(style_command)
        # 根据风格切换表情
        if dm.current_style == "warm":
            furhat.gesture(name="BigSmile")
            furhat.set_voice(name="Ivy")
            print(f"[Robot]: Okay, I've switched to {dm.current_style} mode."
                  f"I'm really glad to be here with you. Job searching can bring all kinds of feelings. How are you feeling today?")
            furhat.say(text=f"Okay, I've switched to {dm.current_style} mode. "
                            f"I'm really glad to be here with you. Job searching can bring all kinds of feelings."
                            f" How are you feeling today?",
                       blocking=True)
        elif dm.current_style == "neutral":
            furhat.gesture(name="Smile")
            furhat.set_voice(name="Ruth-Neural")
            print(f"[Robot]: Okay, I've switched to {dm.current_style} mode."
                  f" Welcome. Emotions affect job search outcomes. Please describe how you feel right now.")
            furhat.say(text=f"Okay, I've switched to {dm.current_style} mode. "
                            f"Welcome. Emotions affect job search outcomes. Please describe how you feel right now.",
                       blocking=True)
        break
    else:
        print(f"[Robot]: Please tell me warm or neutral.")
        furhat.say(text="Please tell me warm or neutral.", blocking=True)



first_round = True
while True:
    result = furhat.listen()
    if not result or not result.message:
        print(f"[Robot]: Sorry, I didn't catch that. Could you repeat?")
        furhat.say(text="Sorry, I didn't catch that. Could you repeat?", blocking=True)
        continue

    user_input = result.message.lower()
    print(f"[User]: {user_input}")

    # 等 1 秒，判断是否还有后续发言（防止误判）
    time.sleep(0.5)
    followup = furhat.listen()

    if followup and followup.message:
        user_input += " " + followup.message.lower()
        print(f"[User continued]: {followup.message}")

    polarity = get_user_emotion(user_input)
    print(f"[Emotion] Detected polarity: {polarity}")

    # 判断退出语句
    exit_phrases = [
        "exit", "quit", "bye", "goodbye", "see you", "have a nice day", "i'm done",
        "no more", "that's all", "i have no more questions",
        "nothing else", "i think that’s it", "we're done","that's it for now", "thanks, that's all","nothing"
    ]
    warm_exit = "Thank you for sharing today — I truly admire your courage. Job searching comes with emotional ups and downs, " \
                "and every step you take is part of your growth. Believe in yourself and give yourself some patience and care. " \
                "I hope this conversation offered you support. You’re always welcome to come back and talk. " \
                "Wishing you a lovely day. Goodbye!"
    neutral_exit = "Session summary: emotional status assessed, key job search challenges identified, strategy suggestions provided."\
                   " Suggested next steps: prioritize and implement one strategy, set a weekly goal and track your progress."\
                   " Feel free to ask if you need anything else. This session is concluded. Best of luck!"
    if any(phrase in user_input for phrase in exit_phrases):
        if dm.current_style == "warm":
            furhat.gesture(name="Wink")
            print(f"[Robot]: {warm_exit}")
            furhat.say(text= warm_exit, blocking=True)
        else:
            furhat.gesture(name="Smile")
            print(f"[Robot]: {neutral_exit}")
            furhat.say(text=neutral_exit, blocking=True)
        break

    # 第一轮：情绪识别 + 主题回应
    if first_round:
        response = handle_emotion_and_topic(user_input, dm.current_style, furhat)
        first_round = False
    else:
        # 后续提问：持续响应用户问题，直到用户说“没有问题了”等
        response = handle_question_and_response(user_input, dm.current_style, furhat)

    print(f"[Robot]: {response}")
    furhat.say(text=response, blocking=True)
    time.sleep(0.2)

stop_logging()