# выражения генераторы или генераторные выражения

numbers = [1, 1, 2, 2, 3, 3]
squares = (i * i for i in numbers)

print(type(squares))

with open('../url-shortener/url_shortener/__init__.py') as f:
    lines = (line.strip() for line in f)
    decors = (d for d in lines if d.find('@') != -1)
    print(list(decors))
