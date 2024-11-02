import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def search_google(payload):
    url = "https://google.serper.dev/search"
    headers = {
      'X-API-KEY': os.getenv('SERPER_API_KEY'),
      'Content-Type': 'application/json'
    }
    payload["location"] = "United States"
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.text
