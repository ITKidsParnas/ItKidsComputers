import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")

        self.expression = ""

        # Поле для отображения результата
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=("Arial", 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.result_var.set(self.expression)
            except Exception as e:
                self.result_var.set("Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
