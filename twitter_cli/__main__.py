from .cli import get_one_tweet
if __name__ == '__main__':
    tw = get_one_tweet("1372519422380797955")
    print(f"\ntwitter : {tw}")