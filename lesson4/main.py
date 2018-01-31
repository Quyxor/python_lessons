'''
Модули:
Исполняемый (запускаемый, главный) модуль

Как импортировать модуль?
* - импортировать целиком
* - частичный импорт
* - включение всех имен (плохой вариант)

Дистрибуция пакетов
'''
# from square_shapes import *
# import square_shapes # импорт целиком
# from square_shapes import (
#     calculate_triangle_area,
#     calculate_circle_area,
#     debug
#     ) # частичный импорт, все имена read only
#
# # print(square_shapes.calculate_square_area(5)) # вызов функции подключенного модуля
# # print(calculate_triangle_area(30, 30, 30))
#
# print(debug)
# print(square_shapes.debug)
# debug = True
# square_shapes.debug = True
# print(debug)
# print(square_shapes.debug)

# import mega_math
# import mega_math.square_shapes
#
# from mega_math import square_shapes
# from mega_math.square_shapes import calculate_triangle_area

from mega_math import square_shapes

print(square_shapes.calculate_square_area(5))
