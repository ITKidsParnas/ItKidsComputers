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
        self.root.bind("<KeyPress", self.change_direction)
        self.update_sneake()

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