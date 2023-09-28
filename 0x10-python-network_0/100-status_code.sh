#!/bin/bash
# sends request pased as an argument
curl -so /dev/null -w "%{http_code}" "$1"
