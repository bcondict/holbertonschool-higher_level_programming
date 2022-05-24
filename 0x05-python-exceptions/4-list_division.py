#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_lenght):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except LookupError:
            print("out if range")
        finally:
            new_list.append(num)
    return new_list
