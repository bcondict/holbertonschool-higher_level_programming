#!/usr/bin/python3
""""""


class MyList(list):
    """"""
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
