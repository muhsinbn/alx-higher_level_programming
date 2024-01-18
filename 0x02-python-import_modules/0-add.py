#!/usr/bin/python3
if __name__ == "__main__":

    # This allows to run code as a script and imported as module

    from add_0 import add

    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
