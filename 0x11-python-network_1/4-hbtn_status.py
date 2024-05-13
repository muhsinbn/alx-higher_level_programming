#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status using
the requests package.
"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
