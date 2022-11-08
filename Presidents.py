import requests
import pytest


url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&t=ha&va=j&ia=web"

response = requests.get(url)

my_json = response.json()
