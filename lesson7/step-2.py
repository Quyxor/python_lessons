# # итераторы

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
person = {
    'name': 'Linus Torvalds',
    'age': 47,
    'is_developer': True
}

it = iter(person)
print(next(it))
print(next(it))
print(next(it))
#
#
# # for i in s:
# # 	print(i)
#DON'T DO IT
# # it = iter(s)
# # while True:
# # 	try:
# # 		next(it)
# # 	except StopIteration:
# # 		break
#
#
#
# # .keys - ключи
# # .values - значения
# # .items - кортеж из двух начений - ключ и значение
# # a = 5
# # b = 8
# # b, a = a, b
#
# # t = (1, 2)
# # a, b = t
# # print(a, b)
#
# # print(person.items())
#
# # for key in person.items():
# # 	print(key, value)
#
#
# # print(type(enumerate(lst)))
#
# # for i, value in enumerate(lst):
# # 	print(i, value)
