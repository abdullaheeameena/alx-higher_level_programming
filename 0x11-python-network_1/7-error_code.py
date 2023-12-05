#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)

