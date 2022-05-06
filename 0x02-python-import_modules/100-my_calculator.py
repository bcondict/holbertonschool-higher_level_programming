#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(argv[1], argv[3], add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(argv[1], argv[3], sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(argv[1], argv[3], mul(a, b)))
        elif argv[2] == "/":
            print("{} / {} = {}".format(argv[1], argv[3], div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
