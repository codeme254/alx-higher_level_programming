#!/bin/bash
# Sends DELETE request to URL passed as the first arg and displays res body
curl -s "$1" -X DELETE
