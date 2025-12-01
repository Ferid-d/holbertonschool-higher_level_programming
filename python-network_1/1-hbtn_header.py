#!/usr/bin/python3
"""Fetches URL and displays X-Request-Id header"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
    if x_request_id:
        print(x_request_id)
