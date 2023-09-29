#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""
if __name__ == "__main__":

    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
