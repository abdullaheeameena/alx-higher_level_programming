#!/usr/bin/python3

import requests
import sys

url = sys.argv[1]
email = {'email': sys.argv[2]}
response = requests.post(url, data=email)
print("Your email is:", response.text)

