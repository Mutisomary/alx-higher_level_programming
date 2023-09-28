#!/bin/bash
# Script that makes a request
curl -X PUT -d "user_id=98" --header "Origin: School" -sL 0:5000/catch_me
