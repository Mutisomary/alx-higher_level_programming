#!/usr/bin/python3
"""
python scri[t that fetches a url using requests package
"""

import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    # display response body
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
