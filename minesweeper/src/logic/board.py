import random
import pygame as pg

from logic.piece import Piece
from logic.board_status import BoardStatus


class Board:
    def __init__(self, size: tuple, mines: int, tile_size: int, board_offset: tuple):
        self.size = size
        self.mine_count = mines
        self.board = self.empty_board()
        self.tile_size = tile_size
        self.status = BoardStatus.NOT_STARTED
        self.offset = board_offset
        self.time_ticks = [0, 0]

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
            if not piece.is_bomb and not self.is_clicked_position(
                position,
                (
                    row * self.tile_size + self.offset[0],
                    col * self.tile_size + self.offset[1],
                ),
            ):
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
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if not (0 <= new_row < self.size[0] and 0 <= new_col < self.size[1]):
                    continue
                piece = self.board[row + i][col + j]
                if piece.clicked or piece.flagged:
                    continue
                piece.reveal()
                self.reveal_empty_tiles(self.board[row + i][col + j])
                if piece.is_bomb:
                    self.end_game()

    def has_started(self):
        return self.status != BoardStatus.NOT_STARTED

    def end_game(self):
        self.status = BoardStatus.GAME_OVER
        self.time_ticks[1] = pg.time.get_ticks()

    def has_lost(self):
        return self.status == BoardStatus.GAME_OVER

    def game_is_running(self):
        return self.status == BoardStatus.RUNNING

    def reset_board(self):
        self.board = self.empty_board()
        self.status = BoardStatus.NOT_STARTED
        self.time_ticks = [0, 0]

    def mines_left(self):
        return self.mine_count - sum(
            piece.flagged for row in self.board for piece in row
        )

    def get_time(self):
        if self.time_ticks[0] == 0:
            return 0
        if self.status == BoardStatus.GAME_OVER:
            return (self.time_ticks[1] - self.time_ticks[0]) // 1000
        if not self.has_started():
            return 0
        return (pg.time.get_ticks() - self.time_ticks[0]) // 1000
