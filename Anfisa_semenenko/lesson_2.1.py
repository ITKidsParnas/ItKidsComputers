password = "kapibara"




while True:
    userinput = input("пароль: ")
    if userinput == password:
        print("верный пароль")
    elif userinput == "exit":
        exit()
    else:
        print("пароль не верный")