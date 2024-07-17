#!/usr/bin/python3
nb = 0
while nb < 99:
    hexa = hex(nb)
    txt = "{} = {}".format(nb, hexa)
    print(txt)
    nb = nb + 1
