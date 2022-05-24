#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    newlist = []
    for i in range(list_lenght):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out if range")
        finally:
            newlist.append(num)
    return newlist
