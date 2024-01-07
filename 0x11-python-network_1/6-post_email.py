#!/usr/share/python3
""" 6. POST an email #1 """

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email = {"email": argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
