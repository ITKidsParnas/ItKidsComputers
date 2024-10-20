import time

d = int(input("Сколько секунд:  "))

while d > 0:
    print(d)
    d -= 1
    time.sleep(1)
