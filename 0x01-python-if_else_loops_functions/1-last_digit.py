#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
length = len(str(number))
last = int(str(number)[length - 1])

if number > 0:
    if last_digit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, last))
    elif last_digit == 0:
        print("Last digit of {} is 0 and is 0".format(number))
    elif last_digit < 6 and last_digit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))
else:
    print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last))
