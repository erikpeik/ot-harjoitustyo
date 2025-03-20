from ui.tile import Tile
from logic.minesweeper import Minesweeper


class GameView:
    def __init__(self, game: Minesweeper, screen):
        self.game = game
        self.screen = screen
        self.tile = Tile(game.board)

    def draw(self):
        top_left = (0, 0)
        for row in self.game.board.get_board():
            for piece in row:
                self.tile.draw(self.screen, top_left, piece)
                top_left = (top_left[0], top_left[1] + self.game.tile_size)
            top_left = (top_left[0] + self.game.tile_size, 0)

    def handle_click(self, position):
        top_left = (0, 0)
        for row in self.game.board.get_board():
            for piece in row:
                self.tile.handle_click(position, top_left, piece)
                top_left = (top_left[0], top_left[1] + self.game.tile_size)
            top_left = (top_left[0] + self.game.tile_size, 0)
