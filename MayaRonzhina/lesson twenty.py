import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.snake = [(200, 200), (200, 210), (200, 220)]
        self.food = self.create_food()
        self.direction = "Up" 
        self.game_over = False
        self.root.bind("<KeyPress>", self.change_direction)
        self.update_snake()

    def create_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0,  39) * 10
        return (x,y)
    
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def update_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction =="Up":
            new_head = (head_x, head_y - 10)
        elif self.direction =="Down":
            new_head = (head_x, head_y + 10)
        elif self.direction =="Left":
            new_head = (head_x - 10, head_y)
        elif self.direction =="Right":
            new_head = (head_x + 10, head_y)

        self.snake = [new_head] + self.snake[:-1]

        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.create_food()

        if new_head in self.snake[1:] or not (0 <= new_head[0] < 400 and 0 <= new_head[1] < 400):
            self.game_over = True

        self.canvas.delete(tk.ALL)
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0],segment[1],segment[0]+10,segment[1]+10, fill="purple")

        self.canvas.create_rectangle(self.food[0],self.food[1],self.food[0]+10,self.food[1]+10, fill="yellow")

        if not self.game_over:
            self.root.after(500, self.update_snake)
        else:
            self.canvas.create_text(200, 200, text= "Молодец!!! Просрал игру", font =("Helvetica", 24))

game = SnakeGame()
game.root.mainloop()