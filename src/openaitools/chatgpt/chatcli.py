import datetime
import openai
import json
import os


openai.api_key = os.environ["CHATGPT_API_KEY"]

data_environ_var = "CHATGPT_CHAT_BKP_DIR"

default_chat_data_folder = os.environ[data_environ_var] if data_environ_var in os.environ else os.path.join(os.environ["HOME"], ".chatgpt")

today = datetime.datetime.now()
year_folder = today.strftime('%Y')
month_folder = today.strftime('%m')
week_folder = today.strftime('%Y.%mW%V')
time_file_name = today.strftime('chat-%Y.%m.%d-%Hh%M')
file_name = f"{time_file_name}.json"

folder_path = os.path.join(default_chat_data_folder, year_folder, month_folder, week_folder)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

messages = []


def get_chatgpt_output(user_input="Hello world!"):
    messages.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chatgpt_output = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chatgpt_output})
    
    data_path = os.path.join(folder_path, file_name)
    with open(data_path, 'w') as file_handler:
         json.dump({"messages": messages}, file_handler)

    return chatgpt_output


def start_chat_loop():
    user_input = input("> ").strip()
    while user_input != "exit" and user_input != "q":
        chatgpt_output = get_chatgpt_output(user_input)
        print(chatgpt_output)
        user_input = input("> ").strip()


if __name__ == '__main__':
    start_chat_loop()    
