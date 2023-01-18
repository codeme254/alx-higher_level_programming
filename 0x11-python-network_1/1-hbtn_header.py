#!/usr/bin/python3
"""
Takes in a url, sends a request to the url and displays value of x-Request-Id
variable found in the header of the response
You must use package urllib and sys
value of variable is different for each request
You don't need to check arguements passed to the script, (number or type)
You must use the with statement
"""

if __name__ == '__main__':
    import sys
    import urllib.request

    destination_url = sys.argv[1]

    with urllib.request.urlopen(destination_url) as resp:
        headers = resp.info()
        print("{}".format(headers.get('X-Request-Id')))
