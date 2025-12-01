#!/usr/bin/python3
"""Sends POST request with letter parameter and processes JSON response"""

import sys
import requests

if __name__ == "__main__":
    # Set q parameter - empty string if no argument given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send POST request
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        # Try to parse JSON response
        json_response = response.json()

        if json_response:  # Check if JSON is not empty
            # Get id and name from JSON
            user_id = json_response.get('id')
            name = json_response.get('name')

            if user_id is not None and name is not None:
                print(f"[{user_id}] {name}")
            else:
                print("No result")
        else:
            print("No result")

    except ValueError:
        # JSON parsing failed
        print("Not a valid JSON")
