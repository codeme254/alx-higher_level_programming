#!/usr/bin/python3
"""Converting from json to an object (Python data structure)"""
import json


def from_json_string(my_str):
    """From Json to a normal python data structure"""
    return json.loads(my_str)
