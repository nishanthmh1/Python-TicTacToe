import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")
        self.center_window()
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (300 / 2)
        y_coordinate = (screen_height / 2) - (350 / 2)
        self.root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Arial", 20), width=6, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=3, pady=3)

        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 12), width=10, command=self.reset_game)
        reset_button.grid(row=3, column=1, pady=10)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, bg="lightblue", state="disabled")
            if self.check_winner():
                if self.current_player == "X":
                    messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                else:
                    messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                self.disable_buttons()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.make_ai_move()

    def make_ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", bg="lightcoral", state="disabled")
        if self.check_winner():
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            self.disable_buttons()
        elif self.is_board_full():
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.disable_buttons()
        else:
            self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner():
            if is_maximizing:
                return -1
            else:
                return 1
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal", bg="SystemButtonFace")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()