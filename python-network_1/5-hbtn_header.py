#!/usr/bin/python3
"""Fetches X-Request-Id header from URL using requests"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
