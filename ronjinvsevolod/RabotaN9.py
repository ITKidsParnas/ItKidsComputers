class Person():
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def sayname(self):
        print("Меня зовут",self.name,"и мне",self.age)

Seva=Person("Seva",9)
Maya=Person("Maya",5)

Seva.sayname()
