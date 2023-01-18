#!/usr/bin/python3
"""
request
"""

from urllib.request import urlopen
import urllib.error
import sys

if __name__ == "__main__":
    destination_url = sys.argv[1]
    try:
        with urlopen(destination_url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))