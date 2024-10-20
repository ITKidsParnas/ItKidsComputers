class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        print("обьект создан")

    def getname(self):
        return self.__name

    def changename(self, name):
        self.__name = name


    def changeage(self,age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимый vозраст")

    def sayname(self):
        print(f"Ьутя зовут {self.__name} и мне {self.__age}")  

Dima = Person("Dima", 130.691538911488902854)

Dima.sayname()

Dima.changename("ne dima")
Dima.changeage(99)

Dima.sayname()

class Student(Person):
    def study(self):
        print(f"{self.getname()} учится")

dimon = Student("dimon", 110907556325)

dimon.sayname()
dimon.study()


