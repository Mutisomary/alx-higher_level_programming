#!/usr/bin/python3
"""using requests module to fetch"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data)
    print(response.text)
