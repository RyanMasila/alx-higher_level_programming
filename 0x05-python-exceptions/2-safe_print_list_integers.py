#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r = 0
    for x in range(0, x):
        try:
            print("{:d}".format(my_list[x]), end="")
            r += 1
        except (ValueError, TypeError):
            continue
        print("")
        return (r)
