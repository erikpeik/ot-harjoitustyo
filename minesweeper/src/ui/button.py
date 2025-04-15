import pygame as pg
import os


class Button:
    def __init__(self, label: str, pos: tuple, height: int, width: int = None):
        self.pos = pos
        self.height = height
        self.width = width
        self.label = label

    def draw(self, screen):
        button_image = pg.image.load(
            os.path.join("src", "assets", "button.png"))
        font_path = os.path.join(
            "src", "assets", "fonts", "Perfect DOS VGA 437.ttf")

        font = pg.font.Font(font_path, self.height // 3 * 2)

        font_width = font.size(self.label)[0]
        self.width = self.width if self.width else font_width + self.height
        button_image = pg.transform.scale(
            button_image, (self.width, self.height))
        text = font.render(self.label, True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(self.pos[0] + self.width // 2,
                    self.pos[1] + self.height // 2)
        )
        screen.blit(button_image, self.pos)
        screen.blit(text, text_rect)

    def is_clicked(self, mouse_pos: tuple) -> bool:
        x, y = mouse_pos
        if (
            x >= self.pos[0]
            and x <= self.pos[0] + self.width
            and y >= self.pos[1]
            and y <= self.pos[1] + self.height
        ):
            return True
        return False
