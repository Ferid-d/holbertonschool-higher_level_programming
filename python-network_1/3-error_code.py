#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib package"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argc[1]
    try:
        with urllib.request.urlopen('url') as response:
        body = response.read()
	print(body.decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
