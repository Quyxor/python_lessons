'''
name*            - имя пакета (продукта)
version*         - версия пакета
description      - краткое описание пакета
long_description - полное описание
url              - веб сайт
license          - лицензия
author           - имя автора
author_email     - email автора
packeges         - пакеты, которые небходимо скопировать (без рекурсии!)
py_modules       - модули, которые необходимо скопировать
install_requires - прямые зависимости от других пакетов
scripts          - запускаемые из командной строки скрипты
'''
from setuptools import setup #, find_packages


setup(
    name='mega-math',
    version='1.0.0',
    description='Collection of maths formulas.',
    url='mysupersite.com',
    license='ZALUPANAGUBE',
    author='Quyxor',
    author_email='mysuperemail@email.com',
    packeges=['mega_math']
)
