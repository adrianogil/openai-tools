import openai
import os


openai.api_key = os.environ["CHATGPT_API_KEY"]


def get_chatgpt_output(user_input="Hello world!", messages=None):
    if not messages:
        messages = []
    messages.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chatgpt_output = completion.choices[0].message.content
    
    return chatgpt_output
