class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("объект создан")

    def getname(self):
        return self.__name

    def changename(self, name):
        self.__name = name
    
    def changeage(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def sayname(self):
        print(f"Меня зовут {self.__name} и мне {self.__age}")

BASHMAK = Person("BASHMAK", 52)

BASHMAK.sayname()

BASHMAK.changename("krutoi BASHMAK")
BASHMAK.changeage(52)

BASHMAK.sayname()

class Student(Person):
    def study(self):
        print(f"{self.getname()} учится")

BASHMAK2 = Student("BASHMAK", 14)

BASHMAK2.sayname()
BASHMAK2.study()