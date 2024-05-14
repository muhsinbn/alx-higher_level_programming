#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
it prints: Error code: followed by the value of the HTTP status code.

Requirements:
- Uses the packages requests and sys
- Does not import packages other than requests and sys
- Does not need to check arguments passed to the script (number or type)

Usage:
    python script.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    # Sends a request to the specfied URL
    resp = requests.get(url)

    # If HTTP status code is greater than or eq to 400 print err code
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
