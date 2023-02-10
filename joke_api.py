import requests
import json
import time
from typing import Dict

# connect to a "real" API

URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke() -> Dict:
    res = requests.get(URL)
    data = res.json()
    return data

def main():
    joke = get_joke()
    print(joke['setup'])
    time.sleep(1)
    print('...')
    time.sleep(3)
    print(joke['punchline'])

if __name__ == "__main__":
    main()
