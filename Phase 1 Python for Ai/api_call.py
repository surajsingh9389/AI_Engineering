"""How to call Api in python"""

import requests

response = requests.get("https://api.github.com/repos/langchain-ai/langchain")

data = response.json()
print(data)