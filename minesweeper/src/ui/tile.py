import pygame as pg
from logic.piece import Piece
from logic.minesweeper import Minesweeper


class Tile:
    def __init__(self, game: Minesweeper):
        self.sprite_sheet = pg.image.load("src/assets/tiles.png")
        self.tile_size = 16
        self.rendered_size = game.tile_size
        self.board = game.board

    def get_tile(self, piece: Piece):
        x = 0
        y = 0

        adjacent_bombs = self.board.calculate_adjacent_bombs(piece)

        if piece.flagged:
            if not piece.is_bomb and self.board.has_ended():
                x = 7
                y = 0
            else:
                x = 2
                y = 0
        elif piece.clicked:
            if piece.is_bomb:
                x = 6
                y = 0
            elif adjacent_bombs > 0:
                x = adjacent_bombs - 1
                y = 1
            else:
                x = 1
                y = 0
        elif piece.is_bomb and self.board.has_ended():
            x = 5
            y = 0

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

    def is_clicked(self, mouse_pos: tuple, top_left: tuple):
        x, y = top_left
        mx, my = mouse_pos
        return x <= mx < x + self.rendered_size and y <= my < y + self.rendered_size

    def handle_click(self, mouse_pos: tuple, top_left: tuple, piece: Piece, action):
        if self.is_clicked(mouse_pos, top_left):
            if action == "reveal":
                if piece.is_bomb:
                    piece.reveal()
                    self.board.end_game()
                else:
                    piece.reveal()
                    self.board.reveal_empty_tiles(piece)
            elif action == "flag":
                piece.flag_piece()
            elif action == "chord":
                self.board.chord_piece(piece)
