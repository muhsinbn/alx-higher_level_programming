#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.

Requirements:
- Uses Basic Authentication with a personal access token as the password
to access your information (only read:user permission is needed).

- The first argument will be your username.
- The second argument will be your password
(in your case, a personal access token as password).

- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
- Does not need to check arguments passed to the script (number or type).
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the Github API endpoint to get user information
    url = 'https://api.github.com/user'

    # Send a GET request to the Github API with Basic Authentication
    resp = requests.get(url, auth=(username, password))

    # Check if request was successful (status code 200)
    if resp.status_code == 200:
        user_info = resp.json()
        print(user_info.get('id'))
    else:
        print("None")
