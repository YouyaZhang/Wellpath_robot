from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

user_input = "I failed the interview. What should I do? Please reply to me in a warm tone"
inputs = tokenizer(user_input, return_tensors="pt")

reply_ids = model.generate(**inputs)
response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

print(response)
