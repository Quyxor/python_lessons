'''
Модуль square_shapes
'''
from math import pi as PI


debug = False


def set_debug(flag):
    global debug
    debug = flag


def calculate_square_area(a):
    '''площадь квадрата'''
    return a ** 2


def calculate_rectangle_area(a, b):
    '''площадь прямоугольника'''
    return a * b


def calculate_triangle_area(a, b, c):
    '''площадь треугольника'''
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculate_circle_area(r):
    '''площадь круга'''
    return PI * r ** 2


__all__ = (
    'calculate_square_area',
    'calculate_circle_area',
    'calculate_triangle_area',
    'calculate_rectangle_area'
) # для импорта по *


if __name__ == '__main__':
    print(__name__)
    print('Здесь должны были быть тесты')
