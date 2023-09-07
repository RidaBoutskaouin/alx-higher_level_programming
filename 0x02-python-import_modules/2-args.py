#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args_len = len(argv) - 1
    if (args_len) == 0:
        print("{:d} arguments.".format(args_len))
    elif (args_len) == 1:
        print("{:d} argument:".format(args_len))
    else:
        print("{:d} arguments:".format(args_len))

    i = 1

    while i <= args_len:
        print("{:d}: {}".format(i, argv[i]))
        i += 1
