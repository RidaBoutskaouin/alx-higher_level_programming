#!/usr/bin/python3
""" 10. My Github! """

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    request = requests.get("https://api.github.com/user",
                           auth=(username, password))

    try:
        json = request.json()
        print(json.get("id"))
    except ValueError:
        print("Not a valid JSON")
