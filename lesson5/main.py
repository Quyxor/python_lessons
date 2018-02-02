'''
Форматы данных

- Pickle (бинарные файлы)
'''
data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus Torvalds',
            'skills': ('C++', 'C', 'Linux'),
            'is_developer': True
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C', 'GNU'),
            'is_developer': True
        }
    ]
}

print('\n\n')

# Pickle
import pickle

with open('users.pickle', 'wb') as f:
	pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
	loaded_data = pickle.load(f)
	print(loaded_data)

print('\n\n')

# Json - javaScript Object Notation
import json

with open('users.json', 'w') as f:
	json.dump(data, f, indent=4)

with open('users.json') as f:
	print(json.load(f))

print('\n\n')

# CSV
import csv

"""
id;name;skills
1;Linus Torvalds;С,С++
2;Richard Stallman;C;GNU
"""

with open('users.csv', 'w') as f:
    # без значения по умолчанию вернется None, если нет ключа
    # data.get('users' or [])
    users = data.get('users', [])
    if users:
        fieldnames = users[0].keys()

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for user in users:
        writer.writerow(user)


with open('users.csv') as f:
	reader = csv.DictReader(f)

	for row in reader:
		print (row)

print('\n\n')

# INI (conf)
# xml (lxml)
# xps




#==================

#SQLite3/2 - База данных в одном файле
