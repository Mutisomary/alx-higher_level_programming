#!/usr/bin/python3
"""sends a request to the url, and displays a value"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(dict(response.info()).get('X-Request-Id'))
