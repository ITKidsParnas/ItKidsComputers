import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab
import pyautogui

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ваше изображение")

        # Создаем холст
        self.canvas = tk.Canvas(root, bg='white', width=512, height=512)
        self.canvas.pack()

        self.color = 'black'  # Начальный цвет для рисования
        self.brush_mode = True  # Режим кисти по умолчанию
        self.brush_size = 5 # Начальный размер кисти
        self.eraser_size = 5  # Начальный размер ластика
        self.canvas.bind("<Button-1>", self.start_draw)  # Начало рисования
        self.canvas.bind("<B1-Motion>", self.draw)  # Рисование при движении мыши

        # Фрейм для инструментов
        self.tools_frame = tk.Frame(self.root)
        self.tools_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Кнопка для кисти
        self.brush_button = tk.Button(self.tools_frame, text='🖊', command=self.set_brush_mode, width=5, height=2)
        self.brush_button.grid(row=0, column=0, padx=5, pady=5)

        # Кнопка для ластика
        self.eraser_button = tk.Button(self.tools_frame, text='🧹', command=self.set_eraser_mode, width=5, height=2)
        self.eraser_button.grid(row=1, column=0, padx=5, pady=5)

        # Ползунок для выбора размера кисти
        self.brush_size_slider = tk.Scale(self.tools_frame, length=120, from_=1, to=50, orient='horizontal', label='Размер кисти', command=self.update_brush_size)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.grid(row=0, column=1, padx=5, pady=5)

        # Ползунок для выбора размера ластика
        self.eraser_size_slider = tk.Scale(self.tools_frame, length=120, from_=1, to=50, orient='horizontal', label='Размер ластика', command=self.update_eraser_size)
        self.eraser_size_slider.set(self.eraser_size)
        self.eraser_size_slider.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка для выбора цвета
        self.color_button = tk.Button(self.tools_frame, text='Выбрать цвет', command=self.choose_color)
        self.color_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.button_save = tk.Button(self.root, text="Сохранить изображение", command=self.save_image)
        self.button_save.pack()

    def choose_color(self):
        # Открываем диалог для выбора цвета
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color  # Устанавливаем выбранный цвет
            self.brush_mode = True  # Переключаемся в режим кисти после выбора цвета

    def set_brush_mode(self):
        # Устанавливаем режим кисти
        self.brush_mode = True

    def set_eraser_mode(self):
        # Устанавливаем режим ластика
        self.brush_mode = False

    def update_brush_size(self, size):
        self.brush_size = int(size)  # Обновляем размер кисти

    def update_eraser_size(self, size):
        self.eraser_size = int(size)  # Обновляем размер ластика

    def start_draw(self, event):
        # Начинаем рисовать
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.brush_mode:
            # Рисуем линию (кисть)
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.brush_size)
        else:
            # Стираем (ластик)
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill='white', width=self.eraser_size)
        
        self.last_x, self.last_y = event.x, event.y
    
    def save_image(self):
    # Открываем диалог для выбора места сохранения
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            x = self.canvas.winfo_rootx()
            y = self.canvas.winfo_rooty()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()