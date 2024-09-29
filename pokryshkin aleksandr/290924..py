a = 0

#for i in range(5):
 #   print(i)
#while a < 5:
#    print (a)s
#    a+=1
PASSWORD = "e"




while True:
    userinput = input("введите пароль: ")
    if userinput == PASSWORD:
        print("верный пароль")
    elif userinput == "exit":
        exit()
    else:
        print("пароль неверный")


