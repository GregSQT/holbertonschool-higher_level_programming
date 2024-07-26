#!/usr/bin/python3

import sys
print('argument list', sys.argv)
nb_args=len(sys.argv)
print(nb_args -1, "argument:")


for i in range(nb_args):
    if i != 0:
        print(i, ":", sys.argv[i])

