#!/bin/bash
# Sends DELETE request to URL passed as the first arg and displays res body
# You have to use curl
curl -s "$1" -X DELETE
