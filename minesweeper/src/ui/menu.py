import os
import pygame as pg
from entities.difficulty import Difficulty
from ui.utils.draw_outline import draw_outline
from ui.frame import Frame
from ui.button import Button


class Menu:
    def __init__(self, screen):
        self._screen = screen
        self._frame = Frame(screen, (800, 600), (0, 0))
        self.easy_button = Button("EASY", (25, 100), 50, 250, 4)
        self.medium_button = Button("MEDIUM", (25, 160), 50, 250, 4)
        self.hard_button = Button("HARD", (25, 220), 50, 250, 4)
        self.stats_button = Button(
            "STATS", (25, 320), 50, 250, 4,
            background_color=(175, 175, 175),
            lighter_color=(240, 240, 240),
            darker_color=(75, 75, 75))
        self.font_path = os.path.join(
            "src", "assets", "fonts", "PixelOperator8-Bold.ttf"
        )
        self._size = screen.get_size()

    def draw(self):
        self._screen.fill(self._frame.gray_color)
        draw_outline((0, 0), self._size, self._screen, False)

        font = pg.font.Font(self.font_path, 24)
        title = font.render("MINESWEEPER", True, (0, 0, 0))
        title_highlight = font.render("MINESWEEPER", True, (100, 100, 100))
        title_rect = title.get_rect(center=(150, 50))
        for i in range(1, 4):
            title_highlight_rect = title_highlight.get_rect(
                center=(title_rect.center[0], title_rect.center[1] + i)
            )
            self._screen.blit(title_highlight, title_highlight_rect)

        self._screen.blit(title, title_rect)

        self.easy_button.draw(self._screen)
        self.medium_button.draw(self._screen)
        self.hard_button.draw(self._screen)
        self.stats_button.draw(self._screen)

    def button_is_clicked(self, mouse_pos: tuple) -> Difficulty | str | None:
        if self.easy_button.is_clicked(mouse_pos):
            return Difficulty.EASY
        if self.medium_button.is_clicked(mouse_pos):
            return Difficulty.MEDIUM
        if self.hard_button.is_clicked(mouse_pos):
            return Difficulty.HARD
        if self.stats_button.is_clicked(mouse_pos):
            return "stats"
        return None
