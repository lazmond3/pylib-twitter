import os
import requests
from .base64_util import base64_encode_str

CONSUMER_KEY=os.getenv("CONSUMER_KEY")
CONSUMER_SECRET=os.getenv("CONSUMER_SECRET")
TOKEN=os.getenv("TOKEN")
TOKEN_SECRET=os.getenv("TOKEN_SECRET")

if not all([
    CONSUMER_KEY,
    CONSUMER_SECRET,
    TOKEN,
    TOKEN_SECRET ]):
    pass
    # print("Specify all env: CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET")
    # exit(0)

def make_basic(consumer_key: str, consumer_secret: str) -> str:
    concat = f"{consumer_key}:{consumer_secret}"
    converted = base64_encode_str(concat)
    return converted

def get_auth(url: str, basic: str):
    headers = {"Authorization": f"Basic {basic}"}
    payload = {"grant_type": "client_credentials"}
    r = requests.post(url, headers=headers, params=payload)

    print(r)
    print("-------")
    print(r.text)
    with open("dump.json", "w") as f:
        f.write(r.text)

def get_auth2():
    if not all([
        CONSUMER_KEY, CONSUMER_SECRET
    ]):
        print("specify consumer key/secret")
        exit(1)

    basic = make_basic(CONSUMER_KEY, CONSUMER_SECRET)
    print(basic)
    url = "https://api.twitter.com/oauth2/token"
    get_auth(url, basic)

if __name__ == '__main__':
    pass    