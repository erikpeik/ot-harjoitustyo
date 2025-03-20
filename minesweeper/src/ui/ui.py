import pygame as pg
from logic.minesweeper import Minesweeper
from ui.gameview import GameView


class UI:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Minesweeper")
        self.current_scene = "game"
        self.game = None
        self.screensize = ()
        self.game_view = None
        self.clock = pg.time.Clock()

    def run(self):
        self.run_game()

    def run_game(self):
        self.current_scene = "game"
        self.game = Minesweeper()

        screen = pg.display.set_mode(self.game.board_size)
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    position = pg.mouse.get_pos()
                    self.game_view.handle_click(position, event.button)
            self.get_game_view(screen)
        pg.quit()

    def get_game_view(self, screen):
        self.game_view = GameView(self.game, screen)
        self.game_view.draw()
        self.clock.tick(60)
        pg.display.flip()
