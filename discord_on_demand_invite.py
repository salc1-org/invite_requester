import requests
from dotenv import load_dotenv
import os
load_dotenv()

url = "https://discord.com/api/v7/channels/436406634206461953/invites"

token = os.environ["TOKEN"]

headers = {
    "authorization": f"Bot {token}",
    "User-Agent": "DiscordBot (https://github.com/salc1-org/salbot, 0.0.1)",
    }

data = {
    "max_age": 240, #seconds
    "max_uses": 1,
    "unique": True,
}

def get_invite():
    resp = requests.post(url, json=data, headers=headers)
    j = resp.json()
    return j["code"]