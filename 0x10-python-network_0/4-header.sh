#!/bin/bash
# Sends a GET request to a URL, includes X-School-User-Id header, and displays
curl -sH "X-School-User-Id: 98" "$1"
