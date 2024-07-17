#!/usr/bin/python3

#import string
#for alpha_letters in string.ascii_lowercase:
#    if alpha_letters not in 'qe':
#       print(alpha_letters, end="")

for letter_code in range(ord('a'), ord('z')+1):
    letter = chr(letter_code)
    if letter not in "qe":
        print(letter, end="")
