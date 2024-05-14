#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter,
and finally displays the body of the response.

Requirements:
- Uses the packages requests and sys
- Does not import packages other than requests and sys
- The email must be sent in the variable email
- Does not need to error check arguments passed to the script (number or type)

Usage:
    python script.py <URL> <EMAIL>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the data to be sent in the POST request
    data = {'email': email}

    # Send a POST request to the URL with the email as a para,eter
    resp = requests.post(url, data=data)

    # Display the body of the response
    print(resp.text)
