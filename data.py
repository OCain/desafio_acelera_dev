import requests
import json

TOKEN = ''


def get_data():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
    params = {'token': TOKEN}
    r = requests.get(url, params=params)
    return r.json()


def save_file(data):
    with open('answer.json', 'w') as outfile:
        json.dump(data, outfile)


def send_file():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+TOKEN
    file = {'answer': open('answer.json', 'rb')}
    r = requests.post(url, files=file)
    print(r.text)
    print(r.status_code)
    print(r.raise_for_status())
