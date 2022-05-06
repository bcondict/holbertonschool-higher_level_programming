#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    elif argv[3] != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        a = int(argv[2])
        b = int(argv[4])
        if argv[3] == "+":
            print("{} + {} = {}".format(argv[2], argv[4], add(a, b)))
        elif argv[3] == "-":
            print("{} - {} = {}".format(argv[2], argv[4], sub(a, b)))
        elif argv[3] == "*":
            print("{} * {} = {}".format(argv[2], argv[4], mul(a, b)))
        else:
            print("{} / {} = {}".format(argv[2], argv[4], div(a, b)))
        return 0
