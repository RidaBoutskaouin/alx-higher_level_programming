#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded
in utf-8)."""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    req = Request(argv[1], urlencode({"email": argv[2]}).encode("ascii"))
    with urlopen(req) as res:
        print(res.read().decode("utf-8"))
