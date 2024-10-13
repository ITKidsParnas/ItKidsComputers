import tkinter as tk

def create_winlocker():
    root= tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background="black")
    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

if __name__=="__main__":
    create_winlocker()