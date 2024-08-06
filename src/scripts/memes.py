"""
Memes control module
"""

import re

import requests

def get_meme() -> list:
    """
    Get a list of memes url
    """

    url = "https://tenor.com/es/search/memes-gifs"
    response = requests.get(url, timeout=10)
    content = response.text
    pattern = r"https://media.tenor.com/[\w.]*"
    image_url_list = re.findall(pattern, str(content))
    return image_url_list
