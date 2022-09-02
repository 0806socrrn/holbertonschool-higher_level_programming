#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL """
if __name__ == '__main__':
    import requests
    import sys
    para = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=para)
    print(r.text)
