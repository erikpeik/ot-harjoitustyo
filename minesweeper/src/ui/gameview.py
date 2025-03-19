from ui.tile import Tile


class GameView:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.tile = Tile()

    def draw(self):
        top_left = (0, 0)
        for row in self.game.board.getBoard():
            for piece in row:
                self.tile.draw(self.screen, top_left, piece)
                top_left = (top_left[0], top_left[1] + self.game.tile_size)
            top_left = (top_left[0] + self.game.tile_size, 0)
