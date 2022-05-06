#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    counter = 1
    result = 0
    while counter != len(argv):
        result += int(argv[counter])
        counter += 1
    print("{}".format(result))
