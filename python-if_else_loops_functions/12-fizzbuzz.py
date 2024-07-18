#!/usr/bin/python3
def fizzbuzz():
    nb = 1
    while nb < 101:
        if nb % 3 == 0:
            print("Fizz", end=" ")
        elif nb % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(nb), end=" ")
        nb = nb + 1
