import requests

def upload_pdf(pdf_path):
    files = [
        ('file', ('file', open(pdf_path, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'x-api-key': 'sec_xxxxxx'
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        print('Source ID:', response.json()['sourceId'])
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
