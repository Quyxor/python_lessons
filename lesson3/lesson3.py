# Функции
def foo():
    pass

func = foo #переложили функцию в переменную
foo()

# Зачем функции аргументы?
def foo_q(bar):
    print('Hello, {}!'.format(bar)) #шаблон, лучше чем склейка через +

foo_q(2)

# Как передавать аргументы
## Два способа:
## - по значению (копия) неизменяемый тип данных
## - по ссылке изменяемый тип данных
def parse(src, output):
    #src - str
    #output - list
    src = src.strip('.')

    for i in src.split():
        output.append(i)

s = 'Fuck the world'
lst = []
parse(s, lst)
print(s)
print(lst)

# Значения аргументов по умолчанию (может быть только неизменяемого типа)
def foo_w(b, bar=2):
    return b ** bar, b, bar

print(foo_w(4))
y, u, i = foo_w(100)
print(y, u, i)

# Переменное количество аргументов - *args (tuple), одна *
def summa(*args):
    return sum(args)

print(summa(1, 2))
print(summa(1, 2, 1, 44))

# Именованные аргументы
foo_w(bar=100, b=0.5)

def summa_n(*args, **kwargs):
    print(type(args), args)     # tuple
    print(type(kwargs), kwargs) # dict

summa_n(1, 2, 3, 4, a=1, b='beda', c=False)

args = (10, 11, 12)
kwargs = {'x': 100, 'y': -100}
summa_n(*args, **kwargs)

# Замыкания
def trim(chars=None): # функция каррирования или частичного применения
    # замкнутая область видимости (переменные в замкнутой области не уничтожаются)
    def foo_r(s):
        return s.strip(chars)
    return foo_r

spaces_trim = trim()
slashes_trim = trim('\\/|')

print(spaces_trim)
print(spaces_trim('       fff '))
print(trim()('       uuu'))

print(slashes_trim)
print(slashes_trim('//tasks|\\'))

# Области видимости переменных и время их жизни
# - глобальная область видимости (стараться избегать глобальных переменных)
# - локальная область видимости (функции, классы)
global_g = 666

def wrapper():
    external = 777

    def foo_e():
        global global_g
        nonlocal external # only Python3

        global_g = 777
        external = 888

    foo_e()

    print(external, global_g)

#foo_e()
wrapper()

# Анонимная функция
sqrt = lambda x, y=0.5: x ** y
x = 9
print('Корень числа {} = {}'.format(x, sqrt(x)))

lst = [8, 1, 3, 4, 5, 2, 10]
print('--------------------')
lst = list(filter(lambda e: e % 2, lst))
lst = list(map(lambda e: e ** 2, lst))

print(lst)

#Рекурсивная функция
def factorial(n):
    # прямая рекурсия
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(100))

#косвенная рекурсия
'''
def a():
    b()

def b():
    a()
'''
