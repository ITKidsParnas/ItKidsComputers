import tkinter as tk

class CookieClicker:
    def __init__(self, master):
        self.master = master
        self.master.title("Куки-кликер")

        self.cookies = 0
        self.cookies_per_click = 1
        self.autoclickers = 0
        self.grandmas = 0
        self.farms = 0
        self.mines = 0
        self.cookies_per_second = 0
        self.autoclicker_bonus = 0.1
        self.grandma_bonus = 5
        self.farm_bonus = 25  # Количество печенек в секунду от одной фермы
        self.mine_bonus = 100  # Количество печенек в секунду от одной шахты

        # Начальные стоимости
        self.upgrade_cost = 10
        self.autoclicker_cost = 50
        self.grandma_cost = 100
        self.farm_cost = 1000  # Изменена стоимость фермы
        self.mine_cost = 5000  # Стоимость шахты

        # Создаем фрейм для скроллинга
        self.scroll_frame = tk.Frame(master)
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)

        # Создаем канвас для скроллинга
        self.canvas = tk.Canvas(self.scroll_frame)
        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Метка для отображения количества печенек
        self.cookie_label = tk.Label(self.scrollable_frame, text="Печеньки: 0", font=("Arial", 24))
        self.cookie_label.pack(pady=20)

        # Метка для отображения печенек в секунду
        self.cookies_per_second_label = tk.Label(self.scrollable_frame, text="Печенек в секунду: 0.0", font=("Arial", 20))
        self.cookies_per_second_label.pack(pady=20)

        # Кнопка для клика
        self.click_button = tk.Button(self.scrollable_frame, text="Кликни на печеньку!", command=self.click_cookie, font=("Arial", 20))
        self.click_button.pack(pady=20)

        # Метка для отображения улучшений
        self.upgrade_label = tk.Label(self.scrollable_frame, text=f"Улучшение: {self.cookies_per_click} печенек за клик (стоимость: {self.upgrade_cost})", font=("Arial", 20))
        self.upgrade_label.pack(pady=20)

        # Кнопка для покупки улучшения
        self.upgrade_button = tk.Button(self.scrollable_frame, text="Купить улучшение", command=self.buy_upgrade, font=("Arial", 20))
        self.upgrade_button.pack(pady=20)

        # Метка для автокликеров
        self.autoclicker_label = tk.Label(self.scrollable_frame, text=f"Автокликеры: {self.autoclickers} (стоимость: {self.autoclicker_cost})", font=("Arial", 20))
        self.autoclicker_label.pack(pady=20)

        # Кнопка для покупки автокликера
        self.autoclicker_button = tk.Button(self.scrollable_frame, text="Купить автокликер", command=self.buy_autoclicker, font=("Arial", 20))
        self.autoclicker_button.pack(pady=20)

        # Метка для бабушек
        self.grandma_label = tk.Label(self.scrollable_frame, text=f"Бабушки: {self.grandmas} (стоимость: {self.grandma_cost})", font=("Arial", 20))
        self.grandma_label.pack(pady=20)

        # Кнопка для покупки бабушки
        self.grandma_button = tk.Button(self.scrollable_frame, text="Купить бабушку", command=self.buy_grandma, font=("Arial", 20))
        self.grandma_button.pack(pady=20)

        # Метка для ферм
        self.farm_label = tk.Label(self.scrollable_frame, text=f"Фермы: {self.farms} (стоимость: {self.farm_cost})", font=("Arial", 20))
        self.farm_label.pack(pady=20)

        # Кнопка для покупки фермы
        self.farm_button = tk.Button(self.scrollable_frame, text="Купить ферму", command=self.buy_farm, font=("Arial", 20))
        self.farm_button.pack(pady=20)

         # Метка для шахт (новая метка)
        self.mine_label = tk.Label(self.scrollable_frame, text=f"Шахты: {self.mines} (стоимость: {self.mine_cost})", font=("Arial", 20))
        self.mine_label.pack(pady=20)

         # Кнопка для покупки шахты (новая кнопка)
        self.mine_button = tk.Button(self.scrollable_frame, text="Купить шахту", command=self.buy_mine, font=("Arial", 20))
        self.mine_button.pack(pady=20)

        # Метка для сообщений об ошибках
        self.error_label = tk.Label(self.scrollable_frame, text="", font=("Arial", 16), fg="red")
        self.error_label.pack(pady=20)

        # Запуск автокликера
        self.master.after(1000, self.auto_click)

    def click_cookie(self):
        self.cookies += self.cookies_per_click
        self.update_display()

    def buy_upgrade(self):
        if self.cookies >= self.upgrade_cost:
            self.cookies -= self.upgrade_cost
            self.cookies_per_click += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Увеличиваем стоимость улучшения
            self.update_display()
            self.error_label.config(text="")
        else:
            self.error_label.config(text="Недостаточно печенек для улучшения!")

    def buy_autoclicker(self):
        if self.cookies >= self.autoclicker_cost:
            self.cookies -= self.autoclicker_cost
            self.autoclickers += 1
            self.autoclicker_cost = int(self.autoclicker_cost * 1.5)  # Увеличиваем стоимость автокликера
            self.update_display()
            self.error_label.config(text="")
        else:
            self.error_label.config(text="Недостаточно печенек для покупки автокликера!")

    def buy_grandma(self):
        if self.cookies >= self.grandma_cost:
            self.cookies -= self.grandma_cost
            self.grandmas += 1
            self.grandma_cost = int(self.grandma_cost * 1.5)  # Увеличиваем стоимость бабушки
            self.update_display()
            self.error_label.config(text="")
        else:
            self.error_label.config(text="Недостаточно печенек для покупки бабушки!")

    def buy_farm(self):
        if self.cookies >= self.farm_cost:
            self.cookies -= self.farm_cost
            self.farms += 1
            self.farm_cost = int(self.farm_cost * 1.5)  # Увеличиваем стоимость фермы
            self.update_display()
            self.error_label.config(text="")
        else:
            self.error_label.config(text="Недостаточно печенек для покупки фермы!")

    def buy_mine(self):   # Новая функция для покупки шахты 
         if self.cookies >= self.mine_cost:
             self.cookies -= self.mine_cost 
             self.mines += 1 
             self.mine_cost = int(self.mine_cost * 1.5)   # Увеличиваем стоимость шахты 
             self.update_display() 
             self.error_label.config(text="")
         else:
             self.error_label.config(text="Недостаточно печенек для покупки шахты!")

    def auto_click(self):
        self.cookies += (self.autoclickers * self.autoclicker_bonus) + (self.grandmas * self.grandma_bonus) + (self.farms * self.farm_bonus)
        self.cookies_per_second = (self.autoclickers * self.autoclicker_bonus) + (self.grandmas * self.grandma_bonus) + (self.farms * self.farm_bonus)
        self.cookies = max(0, self.cookies)
        self.update_display()
        self.master.after(1000, self.auto_click)
        (self.mines * self.mine_bonus)

    def update_display(self):
        self.cookie_label.config(text=f"Печеньки: {int(self.cookies)}")
        self.cookies_per_second_label.config(text=f"Печенек в секунду: {self.cookies_per_second:.1f}")
        self.upgrade_label.config(text=f"Улучшение: {self.cookies_per_click} печенек за клик (стоимость: {self.upgrade_cost})")
        self.autoclicker_label.config(text=f"Автокликеры: {self.autoclickers} (стоимость: {self.autoclicker_cost})")
        self.grandma_label.config(text=f"Бабушки: {self.grandmas} (стоимость: {self.grandma_cost})")
        self.farm_label.config(text=f"Фермы: {self.farms} (стоимость: {self.farm_cost})")
        if hasattr(self, 'mine_label'):
              mine_text=f"Шахты: {self.mines} (стоимость: {self.mine_cost})"
              mine_text.config(text=mine_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = CookieClicker(root)
    root.mainloop()