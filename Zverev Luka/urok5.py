a = int(input("первое число: "))
d = int(input("второе число: "))

choose = int(input(" 1)сложение 2)вычитание 3)умножение: "))

if choose == 1:
    print(a+d)
elif choose == 2:
    print(a-d)
elif choose == 3:
    print(a*d)
else:
    print("неверная команда")