#SQLite3
'''
Базы данных
    * реляционные базы данных
    * объектно-ориентированные (MongoDB), NOSQL
    * графовые БД

СУБД - система управления базами данных
    * MySQL (MariaDB), PostgreSQL
    * Oracle, MS SQL Server

SQLite - база данных в одном файле
SQL - структурный язык запросов
    DDL - Data Definition Language
        - язык описания данных
        - CREATE TABLE
    DML - Data Manipulation Language
        - язык манипулирования данными
        - INSERT INTO
        - UPDATE
        - DELETE
        - SELECT

Запросы
    - запросы на изменение данных
        * INSERT
        * UPDATE
        * DELETE
        * CREATE TABLE
    - запросы на выборку данных
        * SELECT


'''
import sqlite3


# Установка соединения
db = sqlite3.connect(':memory:') # :memory: - БД в оперативе
sql = '''
    CREATE TABLE IF NOT EXISTS grob (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL DEFAULT '',
        active TINYINT NOT NULL DEFAULT 0
    )
'''

# Создание курсора
cursor = db.cursor()

# Выполняем запрос
result = cursor.execute(sql)

sql = '''
    INSERT INTO grob (title) VALUES (?)
'''

cursor.execute(sql, ('Python',))
cursor.execute(sql, ('C++',))

sql = '''
    SELECT id, title, active FROM grob
'''

# если SELECT, то выбранные данные получаем из cursor
cursor.execute(sql)

# получаем все данные в виде списка
print(cursor.fetchall())

db.close()


with sqlite3.connect(':memory:') as connection:
    try:
        cursor = connection.execute(sql)
        print(cursor.fetchall())
    except sqlite3.DatabaseError as err:
        print('ДОБРЕ ПОЖОНТЕ, БОЯРЕН: {}'.format(err))
    finally:
        print('И ПИШОВ БЫ ТЫ')


''' удаление из БД
DELETE FROM table WHERE id = ?
'''
