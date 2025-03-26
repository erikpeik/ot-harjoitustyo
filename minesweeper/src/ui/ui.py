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
        self.game = Minesweeper((9, 9), 10)

        screen = pg.display.set_mode(self.game.frame_size)
        running = True

        left_mouse_down = False
        right_mouse_down = False

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    position = pg.mouse.get_pos()
                    if event.button == 1:
                        left_mouse_down = True
                        if right_mouse_down:
                            self.game_view.handle_click(position, "chord")
                            right_mouse_down = False
                        else:
                            self.game_view.handle_click(position, "reveal")
                    elif event.button == 3:
                        right_mouse_down = True
                        if left_mouse_down:
                            self.game_view.handle_click(position, "chord")
                            left_mouse_down = False
                        else:
                            self.game_view.handle_click(position, "flag")
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        left_mouse_down = False
                    elif event.button == 3:
                        right_mouse_down = False
            self.get_game_view(screen)
        pg.quit()

    def get_game_view(self, screen):
        self.game_view = GameView(self.game, screen)
        self.game_view.draw()
        self.clock.tick(60)
        pg.display.flip()
