import tkinter as tk
from googletrans import Translator

def translate_text():
    translator = Translator()
    input_text = input_text_box.get("1.0", tk.END)
    translated = translator.translate(input_text, dest=language_var.get())
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, translated.text)

# Создание основного окна
root = tk.Tk()
root.title("Переводчик")

# Поле для ввода текста
input_text_box = tk.Text(root, height=10, width=50)
input_text_box.pack()

# Выбор языка перевода
language_var = tk.StringVar(value='en')  # По умолчанию перевод на английский
language_menu = tk.OptionMenu(root, language_var, 'en', 'ru', 'es', 'fr', 'de')
language_menu.pack()

# Кнопка для перевода
translate_button = tk.Button(root, text="Перевести", command=translate_text)
translate_button.pack()

# Поле для вывода перевода
output_text_box = tk.Text(root, height=10, width=50)
output_text_box.pack()

# Запуск приложения
root.mainloop()
