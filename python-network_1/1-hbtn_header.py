#!/usr/bin/python3
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[0]
    with urllib.request.urlopen(url) as response:
        x-request-id = response.getheader('X-Request-Id')
    if x-request-id:
        print(x-request-id)
