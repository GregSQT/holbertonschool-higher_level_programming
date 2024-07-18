#!/usr/bin/python3
"""Scritp de definition d'un square"""


class Square():
    """Definition de la classe Square"""

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
