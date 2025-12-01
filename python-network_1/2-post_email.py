#!/usr/bin/python3
"""Sends POST request with email parameter and displays response"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data to send
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create POST request
    req = urllib.request.Request(url, data=data)
    
    # Send request and get response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
