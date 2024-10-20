class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("обьект оздан")

    def getname(self):
        return self.__name

    def changename(self, name):
        self.__name = name

    def changeage(self, age):
        if 0 < age < 1488:
            self.__age = age
        else:
            print("Недопустимый возвраст")

    def sayname(self):
        print(f"Меня зовут {self.__name} и мне {self.__age}")
MrBeast = Person("MrBeast", 1488)

MrBeast.__name = "MrBeast"

MrBeast.sayname()

MrBeast.changename("Mrb=b==")
MrBeast.changeage(99)

MrBeast.sayname()

class Student(Person):
    def study(self):
        print(f"{self.getname()}учится")

MrCarlik = Student("MrCarlik", 10)

MrCarlik.sayname()
MrCarlik.study()