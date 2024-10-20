class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age



    def sayname(self):
        print(f"Меня зовут {self.__name} и мне {self.__age}")
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def changename(self,name):
        self.__name=name
    def changeage(self,age):
        if 0< age < 100:
        
            self.__age=age
        else:
            print("Неподходящий возраст")

Yaroslav = Person("Yaroslav", 16)

Yaroslav.sayname()
Yaroslav.changename("ne Yaroslav")
Yaroslav.changeage(10)
print(Yaroslav.getname())
Yaroslav.sayname()

class Student(Person):
    def stydy(self):    
        print(f"{self.getname()} учиться")
Yaroslav2 = Student("Yaroslav",17)
Yaroslav2.stydy()