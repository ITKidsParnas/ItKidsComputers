import tkinter
import random

food = ["chocolate", "chips", "milk", "apple"]
room = ["bathroom", "bedroom", "kitchen"]
word = random.choice(food)
lives = 6

root = tkinter.Tk()
root.title("виселица")
root.geometry("500x300")

wordlabel = tkinter.Label(text = word)
wordlabel.pack(pady=5)

entryword = tkinter.Entry(width=30)
entryword.pack(pady=10)

liveslabel = tkinter.Label(text = f"Lives:{lives}")
liveslabel.pack()

root.mainloop()
