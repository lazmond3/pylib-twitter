import os
import json
import requests
from .base64_util import base64_encode_str
from .TwitterImage import convert_twitter, TwitterImage
from typing import cast

CONSUMER_KEY=os.getenv("CONSUMER_KEY")
CONSUMER_SECRET=os.getenv("CONSUMER_SECRET")
TOKEN=os.getenv("TOKEN")
TOKEN_SECRET=os.getenv("TOKEN_SECRET")

# const
TOKEN_FILENAME="dump.json"

if not all([
    CONSUMER_KEY,
    CONSUMER_SECRET,
    TOKEN,
    TOKEN_SECRET ]):
    pass

def make_basic(consumer_key: str, consumer_secret: str) -> str:
    concat = f"{consumer_key}:{consumer_secret}"
    converted = base64_encode_str(concat)
    return cast(str, converted)

def get_auth(url: str, basic: str) -> None:
    headers = {"Authorization": f"Basic {basic}"}
    payload = {"grant_type": "client_credentials"}
    r = requests.post(url, headers=headers, params=payload)

    print(r)
    print("-------")
    print(r.text)
    with open(TOKEN_FILENAME, "w") as f:
        f.write(r.text)

def get_auth_wrapper() -> None:
    if not all([
        CONSUMER_KEY, CONSUMER_SECRET
    ]):
        print("specify consumer key/secret")
        exit(1)

    basic = cast(str, make_basic(CONSUMER_KEY, CONSUMER_SECRET))
    url = "https://api.twitter.com/oauth2/token"
    get_auth(url, basic)

def get_one_tweet(tweet_id: str, is_second: bool = False) -> TwitterImage:
    if not os.path.exists(TOKEN_FILENAME):
        get_auth_wrapper()
    with open(TOKEN_FILENAME) as f:
        s = json.load(f)
        token = s["access_token"]

    url = "https://api.twitter.com/1.1/statuses/show.json"
    params = {"id": tweet_id}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        r = requests.get(url, params=params, headers=headers)
    except Exception:
        if not is_second:
            os.remove(TOKEN_FILENAME)
            get_auth_wrapper()
            # もう一度実行する
            get_one_tweet(tweet_id, True)

    tx = r.text
    with open(f"dump_one_{tweet_id}.json", 'w') as f:
        f.write(tx)
        js = json.loads(tx)

    # キャッシュを利用する.
    # with open(f"dump_one_{tweet_id}.json", 'r') as f:
        # js = json.load(f)

    print(f"tw: {js}")
    tw = convert_twitter(js)
    return tw    


# if __name__ == '__main__':
    # get_oauth1()
    # get_auth_wrapper()
    # get_one_tweet("1372519422380797955", "AAAAAAAAAAAAAAAAAAAAAOAsvwAAAAAAWi4Y1e1OyYVS5LKNDt1DipSgtiw%3DpDoe1KFdeNAxgvYmh1rNdhTChKXpHCYC9Xi7HhkOvCAxczxZ0D")
    # with open("dump_one.json") as f:
    #     js = json.load(f)
    # image = convert_twitter(js)
    # print(image)
