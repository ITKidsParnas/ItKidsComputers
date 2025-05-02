import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Шахматы")

        self.board = self.create_board()
        self.selected_piece = None
        self.selected_piece_position = None

        self.create_widgets()

    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                button = tk.Button(self.root, bg=color, width=6, height=3,
                                   command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row, column=col)
                self.board[row][col] = button

        self.setup_pieces()

    def setup_pieces(self):
        # Простейшая расстановка фигур
        pieces = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        for col in range(8):
            self.board[0][col].config(text=pieces[col])
            self.board[1][col].config(text='♟')  # Черные пешки
            self.board[6][col].config(text='♙')  # Белые пешки
            self.board[7][col].config(text=pieces[col].lower())

    def on_square_click(self, row, col):
        if self.selected_piece:
            # Перемещение фигуры
            self.move_piece(row, col)
        else:
            # Выбор фигуры
            self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.board[row][col].cget("text")
        if piece:  # Если выбрана фигура
            self.selected_piece = piece
            self.selected_piece_position = (row, col)

    def move_piece(self, row, col):
        if self.selected_piece_position:
            old_row, old_col = self.selected_piece_position
            self.board[row][col].config(text=self.selected_piece)
            self.board[old_row][old_col].config(text='')  # Убираем фигуру с прежнего места
            self.reset_selection()

    def reset_selection(self):
        self.selected_piece = None
        self.selected_piece_position = None

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
