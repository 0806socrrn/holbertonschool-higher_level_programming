#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-