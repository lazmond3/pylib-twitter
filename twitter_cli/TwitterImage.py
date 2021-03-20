from dataclasses import dataclass
from typing import List, Dict, Any
from debug import DEBUG

@dataclass
class TwitterImage:
    id_str: str
    image_urls: List[str]

def convert_twitter(dic: Dict[str, Any]) -> TwitterImage:
    if DEBUG:
        print("[convert_twitter] dic: ", dic)
        print("[convert_twitter] extended: ", dic["extended_entities"])
    images = dic["extended_entities"]["media"]
    if DEBUG:
        print(f"[convert_twitter] images: {images}")
    return TwitterImage(
        id_str = dic["id_str"],
        image_urls = list(map(lambda x: x["media_url_https"], images))
    )
