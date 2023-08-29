#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    printed = 0
    for x in range(0, x):
        try:
            print("{}".format(my_list[x]), end="")
            printed += 1
        except:
            break
    print("")
    return printed
