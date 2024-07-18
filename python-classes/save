#!/usr/bin/python3
"""Scritp de definition d'un square"""


class Square():
    """Definition de la classe Square"""

    _size = 0

    def __init__(self, new_size=0):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = new_size

    def area(self):
        return self._size * self._size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
