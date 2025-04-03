from ui.tile import Tile
from ui.frame import Frame
from ui.start_face import StartFace
from ui.number_board import NumberBoard
from ui.titlebar import TitleBar

from logic.minesweeper import Minesweeper
from logic.board_status import BoardStatus

import pygame as pg


class GameView:
    def __init__(self, game: Minesweeper, screen):
        self.game = game
        self.screen = screen
        self.tile = Tile(game.board, game.tile_size)
        self.frame = Frame(screen, game.frame_size, game.board_offset)
        self._start_face = StartFace(game.board, game.frame_size)
        self._number_board = NumberBoard()
        self.title_bar = TitleBar(screen.get_size())

    def draw(self):
        self.frame.draw_frame()
        self._start_face.draw(self.screen)
        self._number_board.draw(
            self.screen, self.game.board.mines_left(), (26, 33 + 30)
        )
        self._number_board.draw(
            self.screen,
            self.game.board.get_time(),
            (
                self.game.frame_size[0] - 26 - self._number_board.rendered_size[0] * 3,
                33 + 30,
            ),
        )
        self.title_bar.draw(self.screen)
        top_left = self.game.board_offset
        for row in self.game.board.get_board():
            for piece in row:
                self.tile.draw(self.screen, top_left, piece)
                top_left = (top_left[0], top_left[1] + self.game.tile_size)
            top_left = (top_left[0] + self.game.tile_size, self.game.board_offset[1])

    def handle_click(self, position: tuple, action: str):
        if not self.game.board.has_started():
            self.game.board.place_bombs(position)
            self.game.board.status = BoardStatus.RUNNING
            self.game.board.time_ticks[0] = pg.time.get_ticks()

        if self.game.board.status == BoardStatus.RUNNING:
            top_left = self.game.board_offset
            for row in self.game.board.get_board():
                for piece in row:
                    self.tile.handle_click(position, top_left, piece, action)
                    top_left = (top_left[0], top_left[1] + self.game.tile_size)
                top_left = (
                    top_left[0] + self.game.tile_size,
                    self.game.board_offset[1],
                )
        self._start_face.handle_click(position)
