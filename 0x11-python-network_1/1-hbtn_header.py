#!/usr/bin/python3
"""Python script that fetches url"""
from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
