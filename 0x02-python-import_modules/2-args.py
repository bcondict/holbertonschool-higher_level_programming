#!/usr/bin/python3
if __name__ == "__main__":
    
    from sys import argv

    argv_count = len(argv) - 1
    if argv_count == 0:
        print("0 arguments.")
    elif argv_count == 1:
        print("{} argument:".format(argv_count, argv))
        print("{}: {}".format(argv_count, argv[1]))
    else:
        print("{} arguments:".format(len(argv), argv))
        for i in range(1, argv_count + 1):
            print("{}: {}".format(i, argv[i]))
