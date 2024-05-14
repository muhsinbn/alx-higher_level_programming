#!/bin/bash
# Sends a request to a URL passed as an arg, display only status code of resp
curl -sI -o /dev/null -w "%{http_code}" "$1"
