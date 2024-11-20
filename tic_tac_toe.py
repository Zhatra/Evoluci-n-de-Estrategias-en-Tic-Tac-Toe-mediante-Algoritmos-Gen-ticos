# tic_tac_toe.py

import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # Representación del tablero

    def reset(self):
        self.board = [' '] * 9

    def display_board(self):
        print(f'''
         {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---+---+---
         {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---+---+---
         {self.board[6]} | {self.board[7]} | {self.board[8]}
        ''')

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def check_winner(self, player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # Filas
            [0,3,6], [1,4,7], [2,5,8],  # Columnas
            [0,4,8], [2,4,6]            # Diagonales
        ]
        for combo in win_conditions:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def get_state(self):
        return ''.join(self.board)

    def set_state(self, state):
        self.board = list(state)
