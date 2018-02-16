'''
ООП. Классы и объекты / cml case !

Зачем нужны свойства?
- свойства, атрибуты, свойства-члены, поля
Свойства - это данные объекта

Зачем нужны методы?
Метод - это функция, объявленная в контексте класса
- методы - поведение объектов
- методы позволяют:
                * менять состояние объекта
                * получать состояние объекта
                * взаимодействовать с объектом

Зачем нужен конструктор?

'''
class Person(object): #обратносовместимый код для 2.7
    '''конструктор'''
    def __init__(self, firstname, lastname, phone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.head = 1

    def get_full_name(self):
        # self - ссылка на текущий экземпляр объекта
        # getters - геттер (получатель)
        return '{} {}'.format(self.firstname, self.lastname)

    def set_firstname(self, firstname):
        # setter - сеттер (установщик)
        set.firstname = firstname


    def kill(self):
        self.head = 0


class Developer(Person):
    '''конструктор'''
    def __init__(self,
                 firstname,
                 lastname,
                 skills,
                 phone=None):
        super().__init__(firstname, lastname, phone)
        # для 2.7 super(Developer, self) 
        self.skills = skills


        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.head = 1



# создание объекта/экземпляра
person_1 = Person('John', 'Rich', '8912345678')

# Чтение значения свойства
print(person_1.get_full_name())
