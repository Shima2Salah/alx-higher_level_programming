#!/usr/bin/python3
"""Python script that fetches url"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.text.headers['X-Request-Id'])
