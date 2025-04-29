import pygame as pg
from ui.utils.draw_outline import draw_outline


class Frame:
    def __init__(self, screen, frame_size, board_offset):
        self.white_color = (255, 255, 255)
        self.gray_color = (192, 192, 192)
        self.dark_gray_color = (128, 128, 128)
        self._frame_size = frame_size
        self._board_offset = board_offset
        self._screen = screen

    def draw_frame(self):
        self._screen.fill(self.gray_color)
        draw_outline((0, 30), self._frame_size, self._screen, False)
        draw_outline(
            (self._board_offset[0] - 4, self._board_offset[1] - 4),
            (self._frame_size[0] - 16 + 3, self._frame_size[1] - 16 + 3),
            self._screen,
            True,
        )
        draw_outline(
            (16 - 3, 16 - 3 + 30),
            (self._frame_size[0] - 16 + 3, self._board_offset[1] - 16 + 3),
            self._screen,
            True,
        )
