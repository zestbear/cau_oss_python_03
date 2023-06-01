# %%

"""
area_rectangle, area_right_triangle, area_ellipse 함수들에서
예외 발생 시 0이하의 값은 입력할 수 없습니다를 출력하도록 변경!
"""

import figure

myline = figure.line(10, 20)
width, height = myline.get_length()
# implement exception handler
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")
rectangle = figure.area_rectangle(width, height)
print(rectangle)

myline.__set_length(20, 30)
width, height = myline.get_length()
# implement exception handler
try:
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("please input positive number for width and height")
triangle = figure.area_right_triangle(width, height)
print(triangle)

myline.set_length(30, 40)
width, height = myline.get_length()
# implement exception handler
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")
ellipse = figure.area_ellipse(width, height)
print(ellipse)