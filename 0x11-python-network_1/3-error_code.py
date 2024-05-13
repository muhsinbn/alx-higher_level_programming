#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
It also handles urllib.error.HTTPError exceptions and prints the HTTP status
code in case of an error.
"""

import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
