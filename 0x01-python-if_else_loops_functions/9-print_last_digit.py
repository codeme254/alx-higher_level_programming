#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    print(number[len(number) - 1], end = "")
    return number[len(number) - 1]
