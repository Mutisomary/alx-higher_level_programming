#!/usr/bin/python3
"""send a post request"""

import requests
import sys


if __name__ == '__main__':
    # Check if an argument is provided, else set q=""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Define the URL
    url = "http://0.0.0.0:5000/search_user"

    # Create a dictionary with the 'q' parameter
    params = {'q': q}

    # Send a POST request to the URL
    response = requests.post(url, data=params)

    # Check if the response has a valid JSON body and is not empty
    try:
        response_json = response.json()
        if response_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get(
                "id"), response_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
