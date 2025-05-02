
import tkinter as tk

def flood_fill(canvas, x, y, target_color, replacement_color):
    if canvas.getpixel((x, y)) != target_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if canvas.getpixel((x, y)) == target_color:
            canvas.putpixel((x, y), replacement_color)

            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

def on_click(event):
    x, y = event.x, event.y
    target_color = canvas.getpixel((x, y))
    replacement_color = "blue"  # Замените на цвет, который хотите использовать для заливки
    flood_fill(canvas, x, y, target_color, replacement_color)

root = tk.Tk()
root.title("Paint")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", on_click)

root.mainloop()
