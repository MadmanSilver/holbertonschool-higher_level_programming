#!/usr/bin/python3
class MagicClass:
    """A circle!"""
    def __init__(self, radius):
        """Initializes radius

        Args:
            radius (int): radius of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calcs area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calcs circumference"""
        return 2 * math.pi * self.__radius
