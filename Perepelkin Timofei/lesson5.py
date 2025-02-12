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

timofei = Person("timofei", 11)

timofei.sayname()

timofei.changename("karasi pleel v tasik, a is tasika pleel v kastromy")
timofei.changeage(52)

timofei.sayname()

class Student(Person):
    def study(self):
        print(f"{self.getname()} учиться")
o = Student("o", 502)


o.sayname()
o.study()