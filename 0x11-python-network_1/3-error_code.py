#!/usr/bin/python3
""" Error code #0 """

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode('utf8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
