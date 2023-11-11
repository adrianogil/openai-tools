import requests
import os

def upload_pdf(pdf_path):
    api_key =  os.environ["CHATPDF_API_KEY"]

    files = [
        ('file', ('file', open(pdf_path, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'x-api-key': api_key
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        print('Source ID:', response.json()['sourceId'])
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
