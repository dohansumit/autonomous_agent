import requests

def call_api(url):

    r = requests.get(url)

    return r.json()