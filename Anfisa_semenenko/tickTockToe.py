import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        
    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=' ', font='Arial 20', width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} выиграл!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Проверка строк
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        
        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
