#!/usr/bin/python3

def islower(c):
    status = c.islower()
    return (status)

def uppercase(str):
    valeur = str
    if valeur == "":
        result = ""
    else:
        lst = []
        for letter in valeur:
            if islower(letter):
                lst.append(letter.swapcase())
            else:
                lst.append(letter)
                result = ''.join(lst)
    print("{}".format(result))

#uppercase("best")
#uppercase("Best School 98 Battery street")
