#!/usr/bin/python3
""" Contains the Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ I'm a Square! Cause I'm not... around! :D """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes values. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the square. """
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ The size of each side of the square. """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the values of the square. """
        if len(args) > 0:
            new = args[:1] + args[1:2] + args[1:]
            super().update(*new)
        else:
            new = kwargs.copy()
            if 'size' in kwargs.keys():
                new['width'] = kwargs['size']
                new['height'] = kwargs['size']
            super().update(**new)

    def to_dictionary(self):
        """ Returns a dictionary representation of the square. """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
