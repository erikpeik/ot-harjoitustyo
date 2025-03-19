from logic.board import Board


class Minesweeper:
    def __init__(self, size=(18, 9), mines=10, tile_size=30):
        self.size = size
        self.board = Board(size, mines)
        self.tile_size = tile_size
        self.board_size = (size[0] * tile_size, size[1] * tile_size)

    def generate_mines(self):
        pass
