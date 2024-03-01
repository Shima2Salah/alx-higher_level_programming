#!/usr/bin/python3
"""displays the body of the response"""
from urllib import request, parse, error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as content:
            response = content.read()        
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        print(response.decode("utf-8"))
