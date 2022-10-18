#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys


def post():
    """status"""
    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(result.text)


if __name__ == "__main__":
    post()