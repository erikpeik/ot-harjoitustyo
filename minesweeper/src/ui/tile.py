import pygame as pg
from logic.piece import Piece
from logic.board import Board


class Tile:
    def __init__(self, board: Board, tile_size):
        self.sprite_sheet = pg.image.load("src/assets/tiles.png")
        self.tile_size = 16
        self.rendered_size = tile_size
        self.board = board

    def get_tile(self, piece: Piece):
        x, y = self.__get_tile_type(piece)
        tile = self.sprite_sheet.subsurface(
            pg.Rect(
                x * self.tile_size,
                y * self.tile_size,
                self.tile_size,
                self.tile_size,
            )
        )
        return pg.transform.scale(tile, (self.rendered_size, self.rendered_size))

    def draw(self, screen, top_left, piece: Piece):
        tile = self.get_tile(piece)
        screen.blit(tile, top_left)

    def handle_click(self, mouse_pos: tuple, top_left: tuple, piece: Piece, action):
        if not self.board.is_clicked_position(mouse_pos, top_left):
            return

        if action == "reveal":
            if piece.is_bomb:
                piece.reveal()
                self.board.end_game()
                return
            piece.reveal()
            self.board.reveal_empty_tiles(piece)
        elif action == "flag":
            piece.flag_piece()
        elif action == "chord":
            self.board.chord_piece(piece)

        self.board.check_win()

    def __get_tile_type(self, piece: Piece):
        adjacent_bombs = self.board.calculate_adjacent_bombs(piece)

        if piece.flagged:
            return 2, 0

        if piece.clicked:
            if piece.is_bomb:
                return 6, 0
            if adjacent_bombs > 0:
                return adjacent_bombs - 1, 1
            return 1, 0

        if piece.is_bomb:
            if self.board.has_won():
                return 2, 0
            if self.board.has_lost():
                return 5, 0

        return 0, 0
