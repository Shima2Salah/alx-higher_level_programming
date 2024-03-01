#!/usr/bin/python3
"""Python script that fetches url"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print("- type: {}".format(type(content)))
        print("- content: {}".format(content))
        print("- utf8 content: {}".format(content.decode("utf8")))
