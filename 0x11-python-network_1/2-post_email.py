#!/usr/bin/python3
"""
Takes in a url and email, sends a POST request to the passed url
email is the parameter, then displays the body of response (decoded in utf-8)
The email must be sent in the email variable
you must use urllib and sys
no need to check the arguements passed (number or type)
Must use the with statement
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    destination_url = sys.argv[1]
    destination_email = sys.argv[2]

    values = {
        "email": destination_email
    }

    values = urllib.parse.urlencode(values).encode('ascii')

    request_ = urllib.request.Request(destination_url, values)
    print(dir(request_))
    with urllib.request.urlopen(request_) as resp:
        print(resp.read().decode('utf-8'))
