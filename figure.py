import math

class line:
    __width  = 0
    __height = 0
    def __init__(self, width, height):
        self.__width  = width
        self.__height = height

    def __set_length(self, width, height):
        self.__width  = width
        self.__height = height

    def get_length(self):
        return self.__width, self.__height
    
def area_rectangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2