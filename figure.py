import math

class line:
    __length = 0
    def __init__(self, length):
        self.__length = length

    def __set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length
    
def area_square(length):
    return length * length

def area_circle(length):
    return length * length * math.pi

def area_regular_triangle(length):
    return length * length * math.sqrt(3) / 4