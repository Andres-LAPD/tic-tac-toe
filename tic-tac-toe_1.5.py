"""
This program is based on the game of tic-tac-toe with a graphical interface.

By Luis Andrés Piñero Diez.
06/08/2024
"""

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = ""
        self.ai = ""
        self.board = [""] * 9
        self.buttons = []
        self.create_interface()

    def create_interface(self):
        # Prompt the player to choose their symbol (X or O)
        self.player = input("Choose your symbol (X/O): ").upper()
        self.ai = "O" if self.player == "X" else "X"
        # Create 9 buttons for the tic-tac-toe grid
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Helvetica", 24), height=2, width=5, command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        # Ensure the move is valid and there's no winner yet
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.player
            self.buttons[index]["text"] = self.player
            # Check if the player has won or if it's a draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Winner: Player {self.player}")
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "Draw")
            else:
                self.make_ai_move()

    def make_ai_move(self):
        # AI makes a move in a random empty spot
        index = random.choice([i for i, x in enumerate(self.board) if x == ""])
        self.board[index] = self.ai
        self.buttons[index]["text"] = self.ai
        # Check if the AI has won or if it's a draw
        if self.check_winner():
            messagebox.showinfo("Game Over", f"Winner: AI ({self.ai})")
        elif "" not in self.board:
            messagebox.showinfo("Game Over", "Draw")

    def check_winner(self):
        # Define winning combinations
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

def main():
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()

if __name__ == '__main__':
    main()
