# генераторы
def generator():
    print('Шаг №1')
    yield 1
    print('Шаг №2')
    yield 2
    print ('Шаг №3')


gen = generator()
print(type(gen))
print(next(gen))
print(next(gen))

for i in generator():
    print('Итерация: {}'.format(i))

def coutdown(n):
	print('Генератор запустился')

	while n:
		yield n
		n -= 1

for i in countdown(5):
	print(i)


def generator_range(start, stop):
    for i in range(start, stop): # Python 3.3* - yield from range(start, stop)
        yield i
