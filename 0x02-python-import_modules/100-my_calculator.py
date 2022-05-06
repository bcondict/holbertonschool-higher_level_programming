#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, * and /")
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
        exit(0)
