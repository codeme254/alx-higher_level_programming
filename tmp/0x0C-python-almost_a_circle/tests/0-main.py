#!/usr/bin/python3
""" 0-main """
from ..base import Base

# https://docs.python.org/3/tutorial/modules.html
# test
if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
