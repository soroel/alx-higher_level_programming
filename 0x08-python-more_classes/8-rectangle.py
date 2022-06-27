#!/usr/bin/python3
"""this module contain the class Rectangle"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            heigh (int): The height of the new Rectangle.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of a rectangle.
            if the height or widht are 0 it returns 0"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        string = []
        for i in range(self.__height):
            string.append(str(self.print_symbol) * self.__width)
        return "\n".join(string)

    def __repr__(self):
        return "{:s}({:d},{:d})".\
            format(self.__class__.__name__, self.__width, self.__height)

    def __del__(self):
        """print a message when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.
            Returns rect_1 if both areas are equals
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
