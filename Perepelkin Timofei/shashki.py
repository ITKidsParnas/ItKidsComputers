import tkinter as tk

class CheckersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Шашки")

        self.board = self.create_board()
        self.selected_piece = None
        self.selected_piece_position = None

        self.create_widgets()
        self.setup_pieces()

    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "brown"
                button = tk.Button(self.root, bg=color, width=6, height=3,
                                   command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row, column=col)
                self.board[row][col] = button

    def setup_pieces(self):
        # Настройка начальной расстановки шашек
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col].config(text='●', fg='black')  # Черные шашки
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col].config(text='●', fg='white')  # Белые шашки

    def on_square_click(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        else:
            self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.board[row][col].cget("text")
        if piece:  # Если выбрана шашка
            self.selected_piece = piece
            self.selected_piece_position = (row, col)

    def move_piece(self, row, col):
        if self.selected_piece_position:
            old_row, old_col = self.selected_piece_position
            # Проверка на допустимость хода
            if self.is_valid_move(old_row, old_col, row, col):
                self.board[row][col].config(text=self.selected_piece, fg=self.board[old_row][old_col].cget("fg"))
                self.board[old_row][old_col].config(text='')  # Убираем шашку с прежнего места
                self.reset_selection()
            else:
                self.reset_selection()  # Сброс выбора, если ход недопустим

    def is_valid_move(self, old_row, old_col, new_row, new_col):
        # Проверка на допустимость хода (простейшая логика)
        if (new_row + new_col) % 2 == 1:  # Должен быть темный квадрат
            if abs(new_row - old_row) == 1 and abs(new_col - old_col) == 1:
                return True
            elif abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
                # Проверка на возможность съесть шашку
                mid_row = (old_row + new_row) // 2
                mid_col = (old_col + new_col) // 2
                mid_piece = self.board[mid_row][mid_col].cget("text")
                if mid_piece and mid_piece != self.selected_piece:  # Если есть шашка противника
                    return True
        return False

    def reset_selection(self):
        self.selected_piece = None
        self.selected_piece_position = None

if __name__ == "__main__":
    root = tk.Tk()
    game = CheckersGame(root)
    root.mainloop()
