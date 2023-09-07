#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    sum = 0
    args_len = len(argv) - 1
    if args_len == 0:
        print("0")
    elif args_len == 1:
        print("{:d}".format(int(argv[1])))
    else:
        i = 1
        while i <= args_len:
            sum += int(argv[i])
            i += 1
        print("{:d}".format(sum))
