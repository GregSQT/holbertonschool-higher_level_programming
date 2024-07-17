#!/usr/bin/python3
nb = 0
while nb < 100:
    if nb < 99:
        print("{:02d}".format(nb), end=", ")
    else:
        print("{:02d}".format(nb))
    nb = nb + 1
