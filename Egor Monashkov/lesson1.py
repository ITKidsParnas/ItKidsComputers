#print("Hello world!")

#text = "Lorem ipsum"

#print(text)

#maths = 1 + 2
#print(maths * 2)


password = "egor"
userinput = input("Введите пароль: ")

if userinput == password:
    print("Пароль верный")
elif userinput == "exit":
    print("Выход из программы")
    exit()
else:
    print("Пароль неверный")