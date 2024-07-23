from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["CHATGPT_API_KEY"],
)

def get_chatgpt_output(user_input="Hello world!", messages=None, model='gpt-4o-mini'):
    if not messages:
        messages = []
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(model=model, messages=messages)
    chatgpt_output = completion.choices[0].message.content

    return chatgpt_output
