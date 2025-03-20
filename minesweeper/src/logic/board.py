import random
from logic.piece import Piece


class Board:
    def __init__(self, size: tuple, mines: int):
        self.__size = size
        self.__mine_count = mines
        self.__board = self.new_board()

    def new_board(self):
        board = [
            [Piece(False) for _ in range(self.__size[1])] for _ in range(self.__size[0])
        ]

        mines_placed = 0
        while mines_placed < self.__mine_count:
            row = random.randint(0, self.__size[0] - 1)
            col = random.randint(0, self.__size[1] - 1)
            if not board[row][col].is_bomb:
                board[row][col] = Piece(True)
                mines_placed += 1

        for row in board:
            for piece in row:
                print("X" if piece.is_bomb else "-", end=" ")
            print()
        return board

    def get_board(self):
        return self.__board
