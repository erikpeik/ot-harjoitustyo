import os
import pygame as pg

from logic.minesweeper import Minesweeper
from entities.difficulty import Difficulty
from ui.gameview import GameView
from ui.menu import Menu
from ui.stats import Stats


class UI:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Minesweeper")
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        self.game = None
        self.menu = None
        self.stats = None
        self.game_view = None
        self.clock = pg.time.Clock()

    def run(self):
        self.run_menu()

    def run_game(self, difficulty: Difficulty):
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

            self.game_view.draw()
            self.clock.tick(60)
            pg.display.flip()
        pg.quit()

    def run_menu(self):
        size = (300, 400)
        screen = pg.display.set_mode(size)
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
            self.menu.draw()
            self.clock.tick(60)
            pg.display.flip()
        pg.quit()

    def run_stats(self):
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
            self.stats.draw()
            self.clock.tick(60)
            pg.display.flip()
        pg.quit()
