import pygame as pg
import os

from logic.minesweeper import Minesweeper
from entities.difficulty import Difficulty
from ui.gameview import GameView
from ui.menu import Menu
from ui.stats import Stats


class UI:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Minesweeper")
        self.current_scene = "game"
        self.game = None
        self.menu = None
        self.stats = None
        self.screensize = ()
        self.game_view = None
        self.clock = pg.time.Clock()
        os.environ["SDL_VIDEO_CENTERED"] = "1"

    def run(self):
        self.run_menu()

    def run_game(self, difficulty: Difficulty):
        self.current_scene = "game"
        self.game = Minesweeper(difficulty)

        screen = pg.display.set_mode(self.game.frame_size)

        left_mouse_down = False
        right_mouse_down = False

        self.game_view = GameView(self.game, screen)

        while self.game.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    continue

                if event.type == pg.MOUSEBUTTONDOWN:
                    position = pg.mouse.get_pos()

                    if event.button == 1:
                        if self.game_view.title_bar.menu_button.is_clicked(position):
                            self.run_menu()
                            self.game.running = False
                            continue

                        left_mouse_down = True
                        if right_mouse_down:
                            self.game_view.handle_click(position, "chord")
                            right_mouse_down = False
                            continue

                        self.game_view.handle_click(position, "reveal")
                        continue

                    if event.button == 3:
                        right_mouse_down = True
                        if left_mouse_down:
                            self.game_view.handle_click(position, "chord")
                            left_mouse_down = False
                            continue

                        self.game_view.handle_click(position, "flag")
                        continue

                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        left_mouse_down = False
                        continue
                    if event.button == 3:
                        right_mouse_down = False
                        continue

            self.get_game_view()
        pg.quit()

    def run_menu(self):
        self.current_scene = "menu"

        size = (300, 400)

        screen = pg.display.set_mode(size)
        pg.display.set_caption("Minesweeper")
        screen.fill((0, 0, 0))
        running = True
        self.menu = Menu(screen)
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    isclicked = self.menu.button_is_clicked(pg.mouse.get_pos())
                    if isclicked == "stats":
                        self.run_stats()
                        running = False
                        continue
                    if isclicked is not None:
                        self.run_game(isclicked)
                        running = False

            self.get_menu_view()
        pg.quit()

    def run_stats(self):
        self.current_scene = "stats"
        screen = pg.display.set_mode((550, 350))

        running = True
        self.stats = Stats(screen)
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    isclicked = self.stats.button_is_clicked(
                        pg.mouse.get_pos())
                    if isclicked:
                        if isclicked == "back":
                            self.run_menu()
                            running = False
                            continue
            self.get_stats_view()

        pg.quit()

    def get_game_view(self):
        self.game_view.draw()
        self.clock.tick(60)
        pg.display.flip()

    def get_menu_view(self):
        self.menu.draw()
        self.clock.tick(60)
        pg.display.flip()

    def get_stats_view(self):
        self.stats.draw()
        self.clock.tick(60)
        pg.display.flip()
