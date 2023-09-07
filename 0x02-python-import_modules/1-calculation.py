#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as my_calc

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, my_calc.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, my_calc.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, my_calc.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, my_calc.div(a, b)))
