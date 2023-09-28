#!/usr/bin/bash
# send a request to a url and display the size of the body
curl -s "$1" | wc -c
