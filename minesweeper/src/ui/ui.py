import pygame as pg
from logic.minesweeper import Minesweeper
from ui.gameview import GameView
from ui.menu import Menu
import os


class UI:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Minesweeper")
        self.current_scene = "game"
        self.game = None
        self.menu = None
        self.screensize = ()
        self.game_view = None
        self.clock = pg.time.Clock()
        os.environ["SDL_VIDEO_CENTERED"] = "1"

    def run(self):
        self.run_menu()

    def run_game(self, difficulty: str):
        self.current_scene = "game"
        if difficulty == "easy":
            self.game = Minesweeper((9, 9), 10)
        elif difficulty == "medium":
            self.game = Minesweeper((16, 16), 40)
        elif difficulty == "hard":
            self.game = Minesweeper((30, 16), 99)

        screen = pg.display.set_mode(self.game.frame_size)

        left_mouse_down = False
        right_mouse_down = False

        while self.game.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
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

    def run_menu(self):
        self.current_scene = "menu"

        screen = pg.display.set_mode((300, 300))
        pg.display.set_caption("Minesweeper")
        screen.fill((0, 0, 0))
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    # check if the mouse is clicked on the button
                    isclicked = self.menu.button_is_clicked(pg.mouse.get_pos())
                    if isclicked:
                        self.run_game(isclicked)
                        running = False

            self.get_menu_view(screen)
        pg.quit()

    def get_game_view(self, screen):
        self.game_view = GameView(self.game, screen)
        self.game_view.draw()
        self.clock.tick(60)
        pg.display.flip()

    def get_menu_view(self, screen):
        self.menu = Menu(screen)
        self.menu.draw()
        self.clock.tick(60)
        pg.display.flip()
