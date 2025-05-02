import tkinter as tk
def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)

    canvas.create_oval(x1,y1,x2,y2,fill="purple",outline="black")
root=tk.Tk()
root.title("Рисовалка")
canvas=tk.Canvas(root,bg="white")
canvas.pack(expand=1,fill=tk.BOTH)
canvas.bind("<B1-Motion>",paint)
root.mainloop()