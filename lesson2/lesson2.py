#lesson2

#Ветвление:
##if else elif

#Блоки кода:
##pass - для пустого блока

a = int(input('Number, bitch: '))
b = int(input('Number two, bitch: '))

if a < b:
    print('Fuck you')
elif a == b:
    print('Go to the hell')
else:
    print('God bless you')

##Тернарный оператор:
# <истина> if <условие> else <ложь>
a = 100 if 1 == 1 else 0

c = input('String, mazafucker: ')
c = c + c if isinstance(c, str) else False
print(c)

#Циклы:
## while
i = 0

while i <= 20:
    print(i)
    i += 5

while i:
    if i == 10:
        break
    elif i == 5:
        continue    # continue - плохой тон

    i += 1

## for
for i in range(20):
    pass

lst = [10, 11, 12, 13]

for i, v in enumerate(lst): # enumerate(*) - получение индексов
    print(i, v)

#Срезы
s = 'Hello, python!'
s[0:5] # тоже что и s[:5] for str&list
lst1 = [1, 2, 3, 4]
lst2 = lst1[:] # копия списка
