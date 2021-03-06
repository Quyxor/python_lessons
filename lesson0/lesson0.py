# coding: utf-8

#lesson_0

#Переменная - переименнованная область оперативной памяти
#Python - регистрозависимый, переменная из несколько слов, разделитель - '_'

#Что зависит от типа данных:
##*Кол-во оперативной памяти
##*Диапазон допустимых значений
##*Допустимые операции
##*Формат представления данных

#Типы данных:
#Скалярные(простые)
###*Целые числа       - int
###*Дробные числа     - float
###*Комплексные числа - complex
###*Логические флаги  - bool
###*Строки            - str
###*Байтовые строки   - bytes
#Структурные(сложные, составные)
###*tuple  - кортежи
###*list   - списки
###*set    - множества
###*dict   - словари
###*object - объекты
#Специальные
###*Ничего - None

#int:
i1 = 10
i2 = 0b001 # Двоинчая СС
i3 = 0o001 # Восьмеричная СС
i4 = 0x00F # Шестнадцатиричная СС

#float:
f1 = 1.1
f2 = 1e6

#complex:
c1 = 3.14j

#bool:
b1 = True
b2 = False

#str:
s1 = 'Hel"lo'
s2 = "Pyt'hon"
s3 = 'Fu\'ck'
s4 = '\tWorld\n'
s5 = '''
				Dratuti
'''
s6 = """Kak '" interesno"""
s7 = u'Kokoko'  # for Python 2 unicode
s8 = r'^\d+$\n' # raw string (for regular)

#bytes:
bs1 = b'Hello'

#None:
abc = None

#object:
'''not now'''

#tuple:
t = (1, 1.2, True, 'x', (1, 2, 3)) # можно положить что угодно, нельзя ничего изменить | описание продукта(id, cost, quantity)
print(t[4]) # обращение по индексу

#list:
l = [1, 1.2, True, 'x', (1, 2, 3), ['x', 'y']] # можно положить что угодно, можно изменять | одна из характеристик в разных значениях
print(l[5]) # обращение по индексу

#set:
s1 = {1, 1.2, True, 'x', 3, 3, 3} # все элементы в множестве - уникальны и упорядочены, при выводе не будут отображены повторы
s2 = set() # пустое множество
print(s)

#dict:
d1 = {} # пустой словарь
d2 = {
        'key_1': 1
        'key_2': {1, 2, 3}
} # индексы - ключи(строки), от значения отделяется ':', от других элементов отделяется запятой, порядок может быть нарушен
