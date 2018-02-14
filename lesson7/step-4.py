# генераторы списков
"""
[expression for item1 in iterable if conditional1
            for item2 in iterable if conditional2
            ...
            for itemN in iterable if conditionalN]
"""
numbers = [1, 1, 2, 2, 3, 3]

squares = [i * i for i in numbers]
odd = [i for i in numbers if i % 2]


points = [(x, y) for x in range(3) for y in range(3)]
print(points)


# генераторы множеств
lst = [1, 1, 2, 2, 3, 3]
s = {i for i in lst}
print(s)


# генераторы словарей
keys = ['id', 'original_url', 'short_url', 'created']
values = [1, 'https://python.org', '/1', '14.02.2018']
#DON'T DO IT
# data = {k: v for i, k in enumerate(keys)
# 			 for j, v in enumerate(values)
# 			 	if i == j}
# print(data)
print(dict(zip(keys, values)))

for key, value in zip(keys, values):
	print(key, value)


data = [
	{
		'id': 1,
		'name': 'Linus Torvalds',
		'is_developer': True
	},
    {
		'id': 2,
		'name': 'Ash Ketchum',
		'is_developer': False
	},
    {
		'id': 1,
		'name': 'Linus Torvalds',
		'is_developer': True
	}
]

persons = {d['id']: d for d in data}
print(persons)
