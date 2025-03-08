import random

secret_number = random.randint(1,100)
guess = None

print("всё вот тебе число давай как-то побыстрее угадывай")

while guess != secret_number:
    guess = int(input("your number:"))

    if guess < secret_number:
        print("больше")
    elif guess > secret_number:
        print("меньше")
    else:
        print("угадал!")