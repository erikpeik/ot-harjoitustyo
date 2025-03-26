import pygame as pg


class Frame:
    def __init__(self, screen, frame_size, board_offset):
        self._white_color = (255, 255, 255)
        self._gray_color = (192, 192, 192)
        self._dark_gray_color = (128, 128, 128)
        self._frame_size = frame_size
        self._board_offset = board_offset
        self._screen = screen

    def draw_frame(self):
        self._screen.fill(self._gray_color)
        self.draw_outline((0, 0), self._frame_size, False)
        self.draw_outline(
            (self._board_offset[0] - 4, self._board_offset[1] - 4),
            (self._frame_size[0] - 16 + 3, self._frame_size[1] - 16 + 3),
            True,
        )
        self.draw_outline(
            (16 - 3, 16 - 3),
            (self._frame_size[0] - 16 + 3, self._board_offset[1] - 16 + 3),
            True,
        )

    def draw_outline(self, top_left, bottom_right, reverse=False, width=5):
        top_left = (top_left[0] + 2, top_left[1] + 2)
        bottom_right = (bottom_right[0] - 2, bottom_right[1] - 2)
        bottom_left = (top_left[0], bottom_right[1])
        top_right = (bottom_right[0], top_left[1])

        pg.draw.line(
            self._screen,
            self._white_color if not reverse else self._dark_gray_color,
            top_left,
            top_right,
            width,
        )
        pg.draw.line(
            self._screen,
            self._dark_gray_color if not reverse else self._white_color,
            top_right,
            bottom_right,
            width,
        )
        pg.draw.line(
            self._screen,
            self._dark_gray_color if not reverse else self._white_color,
            bottom_right,
            bottom_left,
            width,
        )
        pg.draw.line(
            self._screen,
            self._white_color if not reverse else self._dark_gray_color,
            bottom_left,
            top_left,
            width,
        )
