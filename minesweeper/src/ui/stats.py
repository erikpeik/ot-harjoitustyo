import os
import pygame as pg

from ui.button import Button
from ui.utils.draw_outline import draw_outline
from ui.frame import Frame
from services.result_service import result_service


class Stats:
    def __init__(self, screen):
        self._screen = screen
        self._screen_size = screen.get_size()  # (500, 400)
        self._frame = Frame(screen, (800, 600), (0, 0))
        self._font_path = os.path.join(
            "src", "assets", "fonts", "PixelOperator8-Bold.ttf"
        )
        self.results = result_service.get_results()
        self.stats = result_service.get_stats()
        self.back_button = Button("BACK", (10, 10), 30, outline_width=3)

    def draw(self):
        self._screen.fill(self._frame.gray_color)
        draw_outline((0, 0), self._screen_size, self._screen, False)
        font = pg.font.Font(self._font_path, 24)
        title = font.render("STATS", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self._screen_size[0] // 2, 40))
        title_highlight = font.render("STATS", True, (100, 100, 100))
        for i in range(1, 4):
            title_highlight_rect = title_highlight.get_rect(
                center=(title_rect.center[0], title_rect.center[1] + i)
            )
            self._screen.blit(title_highlight, title_highlight_rect)

        self._screen.blit(title, title_rect)
        self.back_button.draw(self._screen)
        self.draw_stats()

    def draw_stats(self):
        font = pg.font.Font(self._font_path, 20)
        stats_texts = [
            f"Total games: {self.stats['total_games']}",
            f"Total wins: {self.stats['total_wins']}",
            f"Total losses: {self.stats['total_losses']}",
            f"Winrate: {self.stats['winrate']:.2f}%",
            f"Top time (EASY): {self.stats['best_result_won'].time:.2f}s" if self.stats[
                'best_result_won'] else "Top time (EASY): N/A",
            f"Top time (MEDIUM): {self.stats['best_result_medium'].time:.2f}s" if self.stats[
                'best_result_medium'] else "Top time (MEDIUM): N/A",
            f"Top time (HARD): {self.stats['best_result_hard'].time:.2f}s" if self.stats[
                'best_result_hard'] else "Top time (HARD): N/A",
        ]

        for i, text in enumerate(stats_texts):
            rendered_text = font.render(text, True, (0, 0, 0))
            text_rect = rendered_text.get_rect(
                center=(self._screen_size[0] // 2, 100 + i * 30))
            self._screen.blit(rendered_text, text_rect)

    def button_is_clicked(self, mouse_pos: tuple) -> str | None:
        if self.back_button.is_clicked(mouse_pos):
            return "back"
        return None
