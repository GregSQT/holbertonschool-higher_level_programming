#!/usr/bin/python3
""" Module de travail"""

"""Definition des variables d'entree"""
def add_integer(a, b=98):
    """Fonction d'addition"""
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    result = a + b

    return (result)

