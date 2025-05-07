import pygame as pg
import os

from ui.utils.draw_outline import draw_outline


class Button:
    def __init__(self,
                 label: str,
                 pos: tuple,
                 height: int,
                 width: int = None,
                 outline_width=5,
                 *,
                 background_color=(192, 192, 192),
                 darker_color=(150, 150, 150),
                 lighter_color=(255, 255, 255),
                 ):
        self.pos = pos
        self.height = height
        self.width = width
        self.label = label
        self._outline_width = outline_width
        self._background_color = background_color
        self._darker_color = darker_color
        self._lighter_color = lighter_color

    def draw(self, screen):
        font_path = os.path.join(
            "src", "assets", "fonts", "PixelOperator8-Bold.ttf")

        font = pg.font.Font(font_path, int(self.height // 2))

        font_width = font.size(self.label)[0]
        self.width = self.width if self.width else font_width + self.height
        text = font.render(self.label, True, (10, 10, 10))
        text_highlight = font.render(self.label, True, (150, 150, 150))
        text_highlight_rect = text_highlight.get_rect(
            center=(self.pos[0] + self.width // 2,
                    self.pos[1] + self.height // 2 + 2)
        )
        text_rect = text.get_rect(
            center=(self.pos[0] + self.width // 2,
                    self.pos[1] + self.height // 2)
        )
        screen.fill(self._background_color,
                    (self.pos[0], self.pos[1], self.width, self.height))
        draw_outline(
            (self.pos[0], self.pos[1]),
            (self.pos[0] + self.width, self.pos[1] + self.height),
            screen,
            False,
            self._outline_width,
            dark_gray_color=self._darker_color,
            white_color=self._lighter_color,
        )
        screen.blit(text_highlight, text_highlight_rect)
        screen.blit(text, text_rect)

    def is_clicked(self, mouse_pos: tuple) -> bool:
        x, y = mouse_pos
        return self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height
