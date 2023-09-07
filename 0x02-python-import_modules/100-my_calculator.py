#!/usr/bin/python3

import calculator_1 as calc
import sys

if __name__ == "__main__":
    operators = ["+", "-", "*", "/"]
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])

        if op in operators:
            if op == "+":
                print("{} + {} = {}".format(a, b, calc.add(a, b)))
                sys.exit(0)
            elif op == "-":
                print("{} - {} = {}".format(a, b, calc.sub(a, b)))
                sys.exit(0)
            elif op == "*":
                print("{} * {} = {}".format(a, b, calc.mul(a, b)))
                sys.exit(0)
            elif op == "/":
                print("{} / {} = {}".format(a, b, calc.div(a, b)))
                sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
