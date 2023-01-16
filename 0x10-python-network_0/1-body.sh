#!/bin/bash
# Takes in a url and sends a get request to the url then dispays body of res
curl -sfL "$1" -X GET
