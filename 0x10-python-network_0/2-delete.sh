#!/bin/bash
# Sends DELETE request to URL passed as the first arg and displays res body
curl -sL "$1" -X DELETE
