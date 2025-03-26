import pygame as pg
from logic.minesweeper import Minesweeper


class StartFace:
    def __init__(
        self,
        game: Minesweeper,
        frame_size: tuple,
    ):
        self._sprite_sheet = pg.image.load("src/assets/faces.png")
        self._face_size = 24
        self._board = game.board
        self._frame_size = frame_size
        self._rendered_size = 48

    def get_face(self):
        x = 0
        y = 0

        if self._board.has_lost():
            x = 4
            y = 0

        face = self._sprite_sheet.subsurface(
            pg.Rect(
                x * self._face_size,
                y * self._face_size,
                self._face_size,
                self._face_size,
            )
        )
        return pg.transform.scale(face, (self._rendered_size, self._rendered_size))

    def draw(self, screen):
        face = self.get_face()
        screen.blit(face, (self._frame_size[0] // 2 - (self._rendered_size // 2), 32))
