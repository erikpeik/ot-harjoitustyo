import pygame as pg


class NumberBoard:
    """Luokka, joka hallitsee numeroiden piirtämistä pelilaudalle.
    """

    def __init__(self):
        self._sprite_sheet = pg.image.load("src/assets/numbers.png")
        self._number_size = (13, 23)
        self.rendered_size = (26, 46)

    def draw(self, screen, score: int, position: tuple):
        score = max(0, score)
        score = min(999, score)
        number = str(score).zfill(3)
        for i, digit in enumerate(number):
            x = position[0] + i * self.rendered_size[0]
            y = position[1]
            number_surface = self.get_number(int(digit))
            screen.blit(number_surface, (x, y))

    def get_number(self, number: int):
        if number < 0 or number > 9:
            raise ValueError("Number must be between 0 and 9")

        x = number * self._number_size[0]
        y = 0

        number_surface = self._sprite_sheet.subsurface(
            pg.Rect(x, y, self._number_size[0], self._number_size[1])
        )
        return pg.transform.scale(number_surface, self.rendered_size)
