#!/usr/bin/python3
"""Contains the Node class."""


class Node:
    """A node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes attributes

        Args:
            data (int): value stored in the node
            next_node (Node): next node in the list

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: value stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: Next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Sorted list of Nodes"""
    def __init__(self):
        """Initializes head to None."""
        self.__head = None

    def sorted_insert(self, value):
        """Adds a new Node into the correct sorted position.

        Args:
            value (int): value to be stored in the new node
        """
        if self.__head is None:
            self.__head = Node(value, None)
        else:
            nav = self.__head
            if nav.data > value:
                self.__head = Node(value, nav)
                return
            while nav.next_node is not None and nav.next_node.data < value:
                nav = nav.next_node
            nav.next_node = Node(value, nav.next_node)

    def __str__(self):
        res = ""
        nav = self.__head
        if nav is not None:
            res += "{}".format(nav.data)
            nav = nav.next_node
        while nav is not None:
            res += "\n{}".format(nav.data)
            nav = nav.next_node
        return res
