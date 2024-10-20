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
            print("недопустимый возраст")

    def sayname(self):
        print(f"меня зовут {self.__name} и мне{self.__age}")

anfisa = Person("anfisa", 12)

anfisa.sayname()

anfisa.changename("karasik v tazik")
anfisa.changeage(52)

anfisa.sayname()

class Student(Person):
    def study(self):
        print(f"{self.getname()} учится")

capybara = Student("capybara", 5)

capybara.sayname()
capybara.study()