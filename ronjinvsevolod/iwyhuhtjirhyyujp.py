import random
secret_number=random.randint(1,100)
guess=None
print("я загадал число от 1 до 100.Попробуй угадать!")
while guess !=secret_number:
    guess=int(input("Ваше число"))


    if guess<secret_number:
        print("Больше")
    elif guess>secret_number:
        print("меньше")
    else:
        print("Угадал")
