import os
import pygame as pg

from ui.utils.draw_outline import draw_outline
from ui.frame import Frame
from services.result_service import result_service


class Stats:
    def __init__(self, screen):
        self._screen = screen
        self._screen_size = screen.get_size()
        self._frame = Frame(screen, (800, 600), (0, 0))
        self.font_path = os.path.join(
            "src", "assets", "fonts", "PixelOperator8-Bold.ttf"
        )
        self.results = result_service.get_results()

    def draw(self):
        self._screen.fill(self._frame.gray_color)
        draw_outline((0, 0), self._screen_size, self._screen, False)
        # draw the title
        font = pg.font.Font(self.font_path, 24)
        title = font.render("STATS", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self._screen_size[0] // 2, 40))
        title_highlight = font.render("STATS", True, (100, 100, 100))
        for i in range(1, 4):
            title_highlight_rect = title_highlight.get_rect(
                center=(title_rect.center[0], title_rect.center[1] + i)
            )
            self._screen.blit(title_highlight, title_highlight_rect)

        self._screen.blit(title, title_rect)
