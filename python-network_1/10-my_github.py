#!/usr/bin/python3
"""Uses GitHub API to display user id with Basic Authentication"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get username and personal access token from command line
    username = sys.argv[1]
    password = sys.argv[2]  # Personal access token

    # GitHub API endpoint for authenticated user
    url = "https://api.github.com/user"

    # Make GET request with Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # Try to get user id from response
    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print(None)
