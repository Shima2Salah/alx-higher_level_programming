#!/usr/bin/python3
"""Python script that fetches url"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    try:
        r = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r['id'], r['name']))
