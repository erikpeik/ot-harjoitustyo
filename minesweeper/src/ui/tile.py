import pygame as pg
from logic.piece import Piece
from logic.board import Board


class Tile:
    def __init__(self, board: Board):
        self.sprite_sheet = pg.image.load("src/assets/tiles.png")
        self.__tile_size = 16
        self.rendered_size = 30
        self.__board = board

    def get_tile(self, piece: Piece):
        x = 1
        y = 0
        if piece.is_bomb:
            x = 2
            y = 0

        adjacent_bombs = self.__board.calculate_adjacent_bombs(piece)

        if adjacent_bombs > 0 and not piece.is_bomb:
            x = adjacent_bombs - 1
            y = 1

        tile = self.sprite_sheet.subsurface(
            pg.Rect(
                x * self.__tile_size,
                y * self.__tile_size,
                self.__tile_size,
                self.__tile_size,
            )
        )
        return pg.transform.scale(tile, (self.rendered_size, self.rendered_size))

    def draw(self, screen, top_left, piece: Piece):
        tile = self.get_tile(piece)
        screen.blit(tile, top_left)
