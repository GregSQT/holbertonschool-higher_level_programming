#!/usr/bin/python3
nb = 1
while nb < 101:
    if nb % 3 == 0:
        return ("Fizz")
    elif nb % 5 == 0:
        return ("Buzz")
    else:
        return (nb)
    nb = nb + 1
