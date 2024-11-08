class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayname(self):
        print("My name", self.name, "и мне", self.age)


Seva_Drift = Person("Seva_Drift", 9)

Oleg = Person("Oleg", 22)

Seva_Drift.sayname()
Oleg.sayname()