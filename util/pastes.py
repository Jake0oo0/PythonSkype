import requests
import json


def post_uxixe(text):
    payload = {
        'content': text
    }

    r = requests.post('http://uxixe.com/api/new_gist', data=json.dumps(payload),
                      headers={"Content-Type": "application/json"})

    return r.json()['html_url']


def post_gist(text):
    payload = {
        "description": "Jake Bot Output",
        "public": True,
        "files": {
            "output.txt": {
                "content": text
            }
        }
    }

    r = requests.post('https://api.github.com/gists', data=json.dumps(payload),
                      headers={"Content-Type": "application/json"})

    return r.json()['html_url']