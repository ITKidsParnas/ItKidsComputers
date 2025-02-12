import tkinter
import random
food=["Бургер","колбаса","макарошки"]
word=random.choice(food)
lives=6
root=tkinter.Tk()
root.title("Виселица")
root.geometry("500*300")

wordlabel=tkinter.Label(text=word)
wordlabel.pack(pady=5)
entryworld=tkinter.Entry(width=30)
entryworld.pack()
liveslabel=tkinter.Label(text=f"Lives:{lives}")
liveslabel.pack()
root.mainloop()

