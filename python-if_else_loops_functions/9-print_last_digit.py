#!/usr/bin/python3

def print_last_digit(number):
    s = str(number)
    lastDigit = s[-1]
    print("{}".format(lastDigit), end="")
    return(lastDigit)
