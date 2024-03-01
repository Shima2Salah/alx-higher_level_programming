#!/usr/bin/python3
"""Python script that fetches url"""
from urllib import request, parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    form_data = bytes(parse.urlencode([('email', email)]), 'utf-8')
    with request.urlopen(url, data=form_data) as content:
        response = content.read()
        print(response.decode("utf-8"))
