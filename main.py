# main.py
# main.py
from furhat_remote_api import FurhatRemoteAPI
from dialogue_manager import DialogueManager
import time

# 连接 Furhat
furhat = FurhatRemoteAPI("localhost")  # 替换成你的 Furhat IP
dm = DialogueManager()

# 欢迎语
furhat.say(text="Hello! I'm here to support you in your job search journey.", blocking=True)
time.sleep(0.5)
furhat.say(text="Before we start, do you prefer a warm tone or a neutral tone?", blocking=True)

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
        furhat.say(text=f"Okay, I've switched to {dm.current_style} mode. Do you have some questions?", blocking=True)
        break
    else:
        furhat.say(text="Please tell me warm or neutral.", blocking=True)

# --- 开始正常对话 ---
while True:
    result = furhat.listen()
    if not result or not result.message:
        furhat.say(text="Sorry, I didn't catch that. Could you repeat?", blocking=True)
        continue

    user_input = result.message.lower()
    print(f"[User]: {user_input}")

    if "exit" in user_input or "quit" in user_input:
        furhat.say(text="Thank you for sharing. Wishing you the best! Goodbye!", blocking=True)
        break

    response = dm.generate_response(user_input)
    print(f"[Robot]: {response}")
    furhat.say(text=response, blocking=True)

    # 根据风格做表情
    if dm.current_style == "warm":
        furhat.gesture(name="Smile")
    elif dm.current_style == "neutral":
        furhat.gesture(name="Nod")

    time.sleep(0.5)