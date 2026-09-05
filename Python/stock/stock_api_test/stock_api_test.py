"""
This is from api https://polygon.io/docs/
The key should be listed in env POLYGON_API_KEY
"""

import requests
import json
import os

key = os.getenv("POLYGON_API_KEY")

url = f"https://api.polygon.io/v3/reference/dividends?apiKey={key}"

response = requests.get(url)

print(json.dumps(response.json(), indent=4))
