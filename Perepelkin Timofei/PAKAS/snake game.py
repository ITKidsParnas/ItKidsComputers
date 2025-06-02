import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра Змейка")

        # Настройки игры
        self.width = 600
        self.height = 400
        self.cell_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'Right'
        self.food = self.place_food()
        self.score = 0

        # Создание холста
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()

        # Управление клавиатурой
        self.root.bind("<Key>", self.change_direction)

        # Запуск игры
        self.update_game()

    def place_food(self):
        x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
        y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.direction = event.keysym

    def update_game(self):
        # Обновление позиции змейки
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= self.cell_size
        elif self.direction == 'Down':
            head_y += self.cell_size
        elif self.direction == 'Left':
            head_x -= self.cell_size
        elif self.direction == 'Right':
            head_x += self.cell_size

        # Проверка на столкновение с границами
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height or (head_x, head_y) in self.snake:
            self.game_over()
            return

        # Проверка на поедание еды
        if (head_x, head_y) == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()  # Удаляем последний сегмент

        # Добавляем новый сегмент в голову
        self.snake.insert(0, (head_x, head_y))

        # Отрисовка
        self.draw()

        # Обновление игры
        self.root.after(100, self.update_game)

    def draw(self):
        self.canvas.delete(tk.ALL)  # Очистка холста
        # Рисуем змейку
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='green')

        # Рисуем еду
        food_x, food_y = self.food
        self.canvas.create_oval(food_x, food_y, food_x + self.cell_size, food_y + self.cell_size, fill='red')

    def game_over(self):
        self.canvas.create_text(self.width // 2, self.height // 2, text="Игра Окончена", fill="white", font=("Arial", 24))
        self.canvas.create_text(self.width // 2, self.height // 2 + 30, text=f"Счет: {self.score}", fill="white", font=("Arial", 16))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
