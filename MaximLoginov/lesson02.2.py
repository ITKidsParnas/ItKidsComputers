#a = 0

#for i in range(5):
#   print(i)

#while a < 5:
#    print(a)
#    a+=1

password = "MY SUMMER CAR"


while True:
    userinput = input("Пароль: ")
    if userinput == password:
        print("Верный пароль") 
    elif userinput == "exit":
        exit()
    else:
        print("пароль неверный")