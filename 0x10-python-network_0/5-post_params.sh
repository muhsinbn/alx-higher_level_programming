#!/bin/bash
# Sends a POST request to a URL with specified variables and displays response
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
