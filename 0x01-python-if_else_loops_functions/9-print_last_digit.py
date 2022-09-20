#!/usr/bin/python3
"""
#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    print(number[len(number) - 1], end="")
    return number[len(number) - 1]
"""


def print_last_digit(number):
    last_digit = (number % 10) if number >= 0 else ((number * -1) % 10)
    print(last_digit, end='')
    return (last_digit)
