password = "privet pypsic"




while True:
    userinput = input("Пароль: ")
    if userinput == password:
        print("Верный пароль")
    elif userinput == "exit":
        exit()
    else:
       print("Пароль не верный") 