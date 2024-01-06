#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://intranet.hbtn.io/status")
    with urlopen(req) as r:
        page = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
