import pygame as pg
from ui.button import Button


class TitleBar:
    """GameViewin yläosa, jossa näppäin takaisin alkuvalikkoon.
    """

    def __init__(self, screen_size: tuple):
        self._screen_size = screen_size
        self._bar_height = 30
        self._text_color = (0, 0, 0)
        self._font = pg.font.Font(None, 24)
        self._bar_color = (220, 220, 220)
        self.menu_button = Button(
            "Menu", (0, 0), self._bar_height, outline_width=3)

    def draw(self, screen):
        pg.draw.rect(
            screen, self._bar_color, (0, 0,
                                      self._screen_size[0], self._bar_height)
        )
        pg.draw.rect(
            screen,
            (190, 190, 190),
            (0, 0, self._screen_size[0], self._bar_height),
            2,
        )
        self.menu_button.draw(screen)
