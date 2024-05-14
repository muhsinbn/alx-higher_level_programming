#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>.

Otherwise:
- Display "Not a valid JSON" if the JSON is invalid.
- Display "No result" if the JSON is empty.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
- Does not need to check arguments passed to the script (number or type).

Usage:
    python script.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    # Get letter from cmd line args or set it to an empty str if no arg is givn
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL
    url = 'http://0.0.0.0:5000/search_user'

    # Send a POST request with the letter as parameter
    resp = requests.post(url, data={'q': q})

    try:
        # Try to parse the response JSON
        data = resp.json()

        if data:
            # If JSON is not empty, display the id and name
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")

    except ValueError:
        # If response JSON not valid
        print("Not a valid JSON")
