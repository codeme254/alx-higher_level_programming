#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length))
        for arg in range(1, length + 1):
            print("{}: {}".format(arg, sys.argv[arg]))
