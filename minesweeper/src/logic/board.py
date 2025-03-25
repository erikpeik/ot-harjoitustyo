import random
from logic.piece import Piece


class Board:
    def __init__(self, size: tuple, mines: int, tile_size: int):
        self.size = size
        self.mine_count = mines
        self.board = self.empty_board()
        self.tile_size = tile_size
        self.is_started = False
        self.game_over = False

    def empty_board(self):
        return [
            [Piece(False, (row, col)) for col in range(self.size[1])]
            for row in range(self.size[0])
        ]

    def place_bombs(self, position: tuple):
        mines_placed = 0
        while mines_placed < self.mine_count:
            row = random.randint(0, self.size[0] - 1)
            col = random.randint(0, self.size[1] - 1)
            piece = self.board[row][col]
            if not piece.is_bomb and not self.is_clicked_position(position, (row, col)):
                self.board[row][col] = Piece(True, (row, col))
                mines_placed += 1

    def is_clicked_position(self, position: tuple, top_left: tuple):
        x, y = top_left
        mx, my = position
        return x <= mx < x + self.tile_size and y <= my < y + self.tile_size

    def get_board(self):
        return self.board

    def calculate_adjacent_bombs(self, piece: Piece) -> int:
        row, col = piece.location
        adjacent_bombs = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not (i == 0 and j == 0)
                    and self.board[row + i][col + j].is_bomb
                ):
                    adjacent_bombs += 1
        return adjacent_bombs

    def reveal_empty_tiles(self, piece: Piece):
        if piece.is_bomb:
            return

        if self.calculate_adjacent_bombs(piece) != 0:
            piece.reveal()
            return

        row, col = piece.location
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not self.board[row + i][col + j].clicked
                ):
                    self.board[row + i][col + j].reveal()
                    self.reveal_empty_tiles(self.board[row + i][col + j])

    def chord_piece(self, piece: Piece):
        row, col = piece.location
        flagged_adjacent = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not (i == 0 and j == 0)
                    and self.board[row + i][col + j].flagged
                ):
                    flagged_adjacent += 1
        if flagged_adjacent != self.calculate_adjacent_bombs(piece):
            return
        for i in range(-1, 2):
            for j in range(-1, 2):
                piece = self.board[row + i][col + j]
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not (i == 0 and j == 0)
                    and not piece.clicked
                    and not piece.flagged
                ):
                    piece.reveal()
                    self.reveal_empty_tiles(self.board[row + i][col + j])
                    if piece.is_bomb:
                        self.end_game()

    def has_started(self):
        return self.is_started

    def end_game(self):
        self.game_over = True

    def has_ended(self):
        return self.game_over
