#!/bin/bash
# Sends a JSON request to a URL with the contents of a file and displays resp
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
