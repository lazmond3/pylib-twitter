import os

CONSUMER_KEY=os.getenv("CONSUMER_KEY")
CONSUMER_SECRET=os.getenv("CONSUMER_SECRET")
TOKEN=os.getenv("TOKEN")
TOKEN_SECRET=os.getenv("TOKEN_SECRET")

if not all([
    CONSUMER_KEY,
    CONSUMER_SECRET,
    TOKEN,
    TOKEN_SECRET ]):
    print("Specify all env: CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET")
    exit(0)