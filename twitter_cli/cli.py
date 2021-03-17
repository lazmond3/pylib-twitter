import twitter
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

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key=CONSUMER_KEY,
                     consumer_secret=CONSUMER_SECRET,
                     token=TOKEN,
                     token_secret=TOKEN_SECRET)

cli = twitter.Twitter(auth=auth)

# twitterへメッセージを投稿する 
# t.statuses.update(status="pythonからtwitterへの投稿テストです！")
def update(text: str)-> None: 
    cli.statuses.update(status=text)
