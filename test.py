from transformers import pipeline

token = "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"

generator = pipeline(
    'text-generation',
    model='lmsys/vicuna-7b-v1.3',
    tokenizer='lmsys/vicuna-7b-v1.3',
    use_auth_token=token
)

prompt = "You are a warm, empathetic coach. Respond kindly to: I feel sad."

output = generator(prompt, max_length=100)
print(output[0]['generated_text'])

