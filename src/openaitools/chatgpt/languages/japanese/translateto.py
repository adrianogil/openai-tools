# openaitools.chatgpt.languages.japanese.translateto
from openaitools.chatgpt.chatcli import get_chatgpt_output

import sys
import os


if len(sys.argv) <= 1:
	str_to_translate = input('> ')
else:
	input_str = sys.argv[1]
	if os.path.isfile(input_str):
		file_path = input_str
		with open(file_path, 'r') as file_handler:
		    str_to_translate = json.load(file_handler)
	else:
		str_to_translate = input_str
prompt = \
f"""Translate the following text to Japanese:

{str_to_translate}
"""
output = get_chatgpt_output(prompt)
print(output)
