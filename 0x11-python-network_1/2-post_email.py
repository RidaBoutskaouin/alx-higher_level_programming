#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded
in utf-8)."""

if __name__ == "__main__":
    """Don't execute if imported"""
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode

    url = argv[1]
    email = urlencode({"email": argv[2]}).encode("ascii")
    req = Request(url, email)
    with urlopen(req) as res:
        print(res.read().decode("utf8"))
