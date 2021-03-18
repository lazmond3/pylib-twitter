import os
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

if __name__ == '__main__':
    print(make_basic("hello", "world"))