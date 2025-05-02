import tkinter as tk
from tkinter import colorchooser, filedialog
from tkinter import *
from tkinter import messagebox
from PIL import ImageGrab
from PIL import Image, ImageTk
import pyautogui

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ваше изображение")
        root.iconbitmap(default="i.ico")
        self.canvas = tk.Canvas(root, bg='white', width=512, height=512, cursor='dot') #crosshair, target
        self.canvas.pack()

        self.color = 'black'  # Начальный цвет для рисования
        self.brush_mode = True  # Режим кисти по умолчанию
        self.brush_size = 5 # Начальный размер кисти
        self.eraser_size = 5  # Начальный размер ластика
        self.rect_size = 5
        self.text = 0
        self.canvas.bind("<Button-1>", self.start_draw)  # Начало рисования
        self.canvas.bind("<B1-Motion>", self.draw)  # Рисование при движении мыши

        #вкладка файл сверху
        root.option_add("*tearOff", FALSE)
        main_menu = Menu(root)
        self.root.config(menu=main_menu) 

        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="📄 Новый холст", command=self.new_image)
        file_menu.add_command(label="💾 Сохранить", command=self.save_image)
        file_menu.add_command(label="📥 Загрузить", command=self.load_image)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Выйти      Alt+F4", command=self.image_exit)

        info_menu = Menu(main_menu, tearoff=0)
        info_menu.add_command(label=" ❕  О программе", command=self.about) 
        info_menu.add_command(label="❔ Описание функций", command=self.podrobnee)                      

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Справка", menu=info_menu)          
        # Фрейм для инструментов
        self.tools_frame = tk.Frame(self.root)
        self.tools_frame.pack(side=tk.LEFT, padx=10, pady=10)

        def update_text():
            # Получаем текст из Entry
            text = text_entry.get()
            # Получаем размер шрифта из Entry
            try:
                font_size = int(font_size_entry.get())
            except ValueError:
                font_size = 12  # Значение по умолчанию, если введено не число
            # Рисуем новый текст с измененным размером
            self.text = self.canvas.create_text(256, 256, text=text, font=("Arial", font_size), fill=self.color)

        text_entry = tk.Entry(root)
        text_entry.pack()

        # поле для ввода размера шрифта
        font_size_entry = tk.Entry(root)
        font_size_entry.pack()

        # кнопку для создания текста
        update_button = tk.Button(root, text="Добавить текст", command=update_text)
        update_button.pack()

        tk.Label(text="Первая строка - текст\nВторая строка - размер").pack(anchor=N, expand=0)

        # Кнопка для кисти
        self.brush_button = tk.Button(self.tools_frame, text='🖊', command=self.set_brush_mode, width=5, height=2, cursor="hand2")
        self.brush_button.grid(row=0, column=0, padx=5, pady=5)

        # Кнопка для ластика
        self.eraser_button = tk.Button(self.tools_frame, text='🧹', command=self.set_eraser_mode, width=5, height=2, cursor="hand2")
        self.eraser_button.grid(row=1, column=0, padx=5, pady=5)

        self.rect_button = tk.Button(self.tools_frame, text='🟨', command=self.set_rect_mode, width=5, height=2, cursor="hand2")
        self.rect_button.grid(row=2, column=0, padx=5, pady=5)

        # Ползунок для выбора размера кисти
        self.brush_size_slider = tk.Scale(self.tools_frame, length=120, from_=1, to=50, orient='horizontal', label='Размер кисти', command=self.update_brush_size)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.grid(row=0, column=1, padx=5, pady=5)

        # Ползунок для выбора размера ластика
        self.eraser_size_slider = tk.Scale(self.tools_frame, length=120, from_=1, to=50, orient='horizontal', label='Размер ластика', command=self.update_eraser_size)
        self.eraser_size_slider.set(self.eraser_size)
        self.eraser_size_slider.grid(row=1, column=1, padx=5, pady=5)

        self.rect_size_slider = tk.Scale(self.tools_frame, length=125, from_=1, to=100, orient='horizontal', label='Размер квадрата', command=self.update_rect_size)
        
        self.rect_size_slider.set(self.rect_size)
        self.rect_size_slider.grid(row=2, column=1, padx=5, pady=5)

        # Кнопка для выбора цвета
        self.color_button = tk.Button(self.tools_frame, text='🎨 Выбрать цвет', command=self.choose_color, cursor="hand2")
        self.color_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.image = None
        self.tk_image = None
        self.image_id = None
        self.image_path = None

        # Масштабирование
        self.scale_var = tk.DoubleVar(value=1.0)
        self.scale_button = tk.Scale(root, length=275, from_=0.1, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, label="Масштаб загруженного изображения", variable=self.scale_var, command=self.scale_image, state=tk.DISABLED)
        self.scale_button.pack(expand=1)
 
    def choose_color(self):
        # Открываем диалог для выбора цвета
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color  # Устанавливаем выбранный цвет
            self.brush_mode = True  # Переключаемся в режим кисти после выбора цвета

    def set_brush_mode(self):
        # Устанавливаем режим кисти
        self.brush_mode = True
        self.rect_mode = False

    def set_eraser_mode(self):
        # Устанавливаем режим ластика
        self.brush_mode = False
        self.rect_mode = False

    def update_brush_size(self, size):
        self.brush_size = int(size)  # Обновляем размер кисти

    def update_eraser_size(self, size):
        self.eraser_size = int(size)  # Обновляем размер ластика

    def update_rect_size(self, size):
        self.rect_size = int(size)  # Обновляем размер ластика

    def set_rect_mode(self):
        self.brush_mode = False
        self.rect_mode = True

    def start_draw(self, event):
        # Начинаем рисовать
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.brush_mode:
            self.canvas.create_oval(event.x - self.brush_size,
                            event.y - self.brush_size,
                            event.x + self.brush_size,
                            event.y + self.brush_size,
                            fill=self.color, outline=self.color)
        elif self.rect_mode:
            self.canvas.create_rectangle(event.x, event.y, event.x + self.rect_size, event.y + self.rect_size, fill=self.color, outline=self.color)
        else:
            #ластик
            self.canvas.create_oval(event.x - self.eraser_size,
                            event.y - self.eraser_size,
                            event.x + self.eraser_size,
                            event.y + self.eraser_size,
                            fill='white', outline='white')
    
        self.last_x, self.last_y = event.x, event.y
    
    def save_image(self):
    # Открываем диалог для выбора места сохранения
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            x = self.canvas.winfo_rootx()
            y = self.canvas.winfo_rooty()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

    def load_image(self):
        # Открытие диалогового окна для выбора изображения
        file_path2 = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")])
        if file_path2:
            self.scale_button.config(state=tk.NORMAL)
            # Загружаем изображение с помощью PIL
            self.image = Image.open(file_path2)
            self.display_image()

    def new_image(self):
        self.canvas.delete("all")

    def display_image(self):
        if self.image is not None:
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)


    def scale_image(self, event):
        if self.image is not None:
            scale_factor = self.scale_var.get()
            new_size = (int(self.image.width * scale_factor), int(self.image.height * scale_factor))
            resized_image = self.image.resize(new_size)
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.canvas.itemconfig(self.image_id, image=self.tk_image)
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def image_exit(self):
        # функция для выхода из программы
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            root.destroy()  # закрывает главное окно

    def about(self):
        messagebox.showinfo("О программе", "Стандартная рисовалка в которой можно побаловатся или порисовать, так-же можно отредактировать изображение")

    def podrobnee(self): #ТУТ БЫЛ ТУРНИК
        messagebox.showinfo("Описание функций", "Кнопка 🖊 - Позволяет после нажатия рисовать выбранным цветом\n\nКнопка 🧹 - После нажатия позволяет стирать нарисованное/добавленное\n\nКнопка 🟨 - Позваляет нарисовать квадрат с выбранным размером\n\nСлайдеры размера кисти/ластика/квадрата - с помощью их можно выбрать размер с которым вы будете рисовать, стирать, или делать квадрат\n\n🎨 Выбрать цвет - после нажатия откроется меню выбора цвета которым вы будете рисовать\n\nПервое окно для текста - впишите сюда желаемый текст\n\nНиже второе окно - впишите сюда размер (цифрами) и после нажмите добавить текст и на экране появится ваш текст\n\nМасштаб загруженного изображение - передвигая слайдер вы меняете размер изображение (об этом во вкладке Файл)\n\n\t\tМеню \"Файл\":\n\n Новый холст - удаляет все нарисованное и создаёт пустое место\n\nСохранить - после нажатие откроется меню выбора места сохранение рисунка как файл\n\nЗагрузить - добавляет на холст картинку которую вы выберете\n\nВыход - закрывает окно программы с последующим предупреждением")  

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()