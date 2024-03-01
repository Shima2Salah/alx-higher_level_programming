
n script that fetches url"""
from urllib import request
import sys
if __name__ == "__main__":
        with request.urlopen("https://alx-intranet.hbtn.io/status") as response
                content = response.read()
                        print("Body response:")
                                print("- type: {}".format(type(content)))
                                        print("- content: b{}".format(content.status_code))
                                                print("- utf8 content: {}".format(content.status_code.decode("utf-8"))):
