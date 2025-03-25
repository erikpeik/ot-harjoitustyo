from logic.board import Board


class Minesweeper:
    def __init__(self, size=(30, 16), mines=99, tile_size=32):
        self.size = size
        self.board = Board(size, mines, tile_size)
        self.tile_size = tile_size
        self.board_size = (size[0] * tile_size, size[1] * tile_size)
