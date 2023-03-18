import openai
import os


openai.api_key = os.environ["CHATGPT_API_KEY"]

messages = []


def get_chatgpt_output(user_input="Hello world!"):
    messages.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chatgpt_output = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chatgpt_output})
    return chatgpt_output


def start_chat_loop():
    user_input = input("> ").strip()
    while user_input != "exit" and user_input != "q":
        chatgpt_output = get_chatgpt_output(user_input)
        print(chatgpt_output)
        user_input = input("> ").strip()


if __name__ == '__main__':
    start_chat_loop()    
