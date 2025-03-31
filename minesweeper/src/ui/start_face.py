import pygame as pg
from logic.board import Board


class StartFace:
    def __init__(
        self,
        board: Board,
        frame_size: tuple,
    ):
        self._sprite_sheet = pg.image.load("src/assets/faces.png")
        self._face_size = 24
        self._board = board
        self._frame_size = frame_size
        self._rendered_size = 48

    def get_face(self):
        x = 0
        y = 0

        if self._board.has_lost():
            x = 4
            y = 0
        elif self._board.has_won():
            x = 3
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
        screen.blit(
            face, (self._frame_size[0] // 2 - (self._rendered_size // 2), 32))

    def is_clicked(self, mouse_pos: tuple):
        x, y = mouse_pos
        if (
            x >= self._frame_size[0] // 2 - (self._rendered_size // 2)
            and x <= self._frame_size[0] // 2 + (self._rendered_size // 2)
            and y >= 32
            and y <= 32 + self._rendered_size
        ):
            return True
        return False

    def handle_click(self, mouse_pos: tuple):
        if self.is_clicked(mouse_pos):
            self._board.reset_board()
