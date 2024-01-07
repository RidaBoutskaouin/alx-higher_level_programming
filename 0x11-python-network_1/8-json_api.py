#!/usr/bin/python3
""" 8. Search API """


if __name__ == "__main__":
    import requests
    from sys import argv

    letter = argv[1] if len(argv) > 1 else ""
    request = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
