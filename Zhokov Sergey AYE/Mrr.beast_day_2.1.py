password = "jopatermenatora228"

userinput = input ("Не верный пороль:")


while True:
if userinput == password:
    print("Верный пороль")
elif userinput == "exit":
    exit()
else:
    print("пороль не верный")