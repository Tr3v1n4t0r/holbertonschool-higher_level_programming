#!/bin/bash
# Write a Bash script that takes in a URL, sends a request ti that URL, and displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length/{print $2}'
