#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL -X PUT --header 'Origin: HolbertonSchool' --data "user_id=98" "0.0.0.0:5000/catch_me"
