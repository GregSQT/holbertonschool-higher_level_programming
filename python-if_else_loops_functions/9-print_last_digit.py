#!/usr/bin/python3

def print_last_digit(number):
    s = str(number)
    lastDigit = s[-1]
    print("{}".format(lastDigit))


#print_last_digit(98)
#print_last_digit(0)
r = print_last_digit(-1024)
print(r)
