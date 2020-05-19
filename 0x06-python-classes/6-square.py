#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for py in range(self.__position[1]):
            print("")
        for y in range(self.__size):
            for px in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print("")
