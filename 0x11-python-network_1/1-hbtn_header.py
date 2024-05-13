#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Requirements:
- Uses the packages urllib and sys
- Does not import packages other than urllib and sys
- The value of the X-Request-Id variable is different for each request
- Does not need to check arguments passed to the script (number or type)
- Uses a with statement
"""

import urllib.request
import sys

url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
