#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
