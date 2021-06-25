from dataclasses import dataclass
from typing import List, Dict, Any
from debug import DEBUG

@dataclass
class TwitterImage:
    id_str: str
    image_urls: List[str]
    video_url: str

def convert_twitter(dic: Dict[str, Any]) -> TwitterImage:
    if DEBUG:
        print("[convert_twitter] dic: ", dic)
        print("[convert_twitter] extended: ", dic["extended_entities"])
    images = dic["extended_entities"]["media"]
    if DEBUG:
        print(f"[convert_twitter] images: {images}")
    
    video_url_inner = None
    if "video_info" in dic["extended_entities"]["media"][0]:
        video_info = dic["extended_entities"]["media"][0]["video_info"]
        video_url_inner = video_info["variants"][0]["url"]
        image_url_inner = dic["extended_entities"]["media"][0]["media_url_https"]
    return TwitterImage(
        id_str = dic["id_str"],
        image_urls = [image_url_inner],
        video_url = video_url_inner
    )
