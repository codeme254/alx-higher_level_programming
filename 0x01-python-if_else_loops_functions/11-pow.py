#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        result = 1
        for i in range(0, b*-1):
            result /= a
    else:
        result = 1
        for i in range(0, b):
            result *= a
    return result
