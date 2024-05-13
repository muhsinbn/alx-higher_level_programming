#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Requirements:
- Uses the packages urllib and sys
- Does not import packages other than urllib and sys
- The email must be sent in the email variable
- Does not need to check arguments passed to the script (number or type)
- Uses a with statement

Usage:
    python script.py <URL> <EMAIL>
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request to the specified URL with email as parameter
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')

    # Display the body of the response
    print(body)
