#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argv[3] != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(argv[2], argv[4], add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(argv[2], argv[4], sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(argv[2], argv[4], mul(a, b)))
        else:
            print("{} / {} = {}".format(argv[2], argv[4], div(a, b)))
        sys.exit(0)
