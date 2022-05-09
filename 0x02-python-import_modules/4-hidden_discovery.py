#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_name = dir(hidden_4)
    for single_name in list_name:
        if single_name[:2] != "__":
            print(single_name)
