#!/usr/bin/python3
"""Sends POST request with email parameter using requests"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request with email parameter
    response = requests.post(url, data={'email': email})

    # Display response body
    print(response.text)
