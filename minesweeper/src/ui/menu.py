import os
import pygame as pg
from ui.frame import Frame
from ui.button import Button


class Menu:
    def __init__(self, screen):
        self._screen = screen
        self._background_color = (255, 255, 255)
        self._frame = Frame(screen, (800, 600), (0, 0))
        self.easy_button = Button("Easy", (25, 100), 50, 250)
        self.medium_button = Button("Medium", (25, 160), 50, 250)
        self.hard_button = Button("Hard", (25, 220), 50, 250)
        self.font_path = os.path.join(
            "src", "assets", "fonts", "Perfect DOS VGA 437.ttf"
        )

    def draw(self):
        self._screen.fill(self._frame.gray_color)
        self._frame.draw_outline((0, 0), (300, 300), False)

        # write the title
        font = pg.font.Font(self.font_path, 30)
        title = font.render("Minesweeper", True, (0, 0, 0))
        title_rect = title.get_rect(center=(150, 50))
        self._screen.blit(title, title_rect)

        self.easy_button.draw(self._screen)
        self.medium_button.draw(self._screen)
        self.hard_button.draw(self._screen)

    def button_is_clicked(self, mouse_pos: tuple) -> str:
        if self.easy_button.is_clicked(mouse_pos):
            return "easy"
        elif self.medium_button.is_clicked(mouse_pos):
            return "medium"
        elif self.hard_button.is_clicked(mouse_pos):
            return "hard"
        return None
