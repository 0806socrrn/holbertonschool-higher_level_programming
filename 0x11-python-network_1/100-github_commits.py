#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge"""
if __name__ == '__main__':
    import sys
    import requests
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo_info = owner_name + "/" + repo_name
    url = "https://api.github.com/repos/" + repo_info + "/commits"
    r = requests.get(url)
    top = r.json()[:10]
    for i in top:
        el = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(el, author))
