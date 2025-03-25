from logic.board import Board


class Minesweeper:
    def __init__(self, size=(9, 9), mines=10, tile_size=32):
        max_height = 30
        max_width = 40
        if size[0] > max_width:
            size = (max_width, size[1])
        if size[1] > max_height:
            size = (size[0], max_height)

        max_bombs = size[0] * size[1] - 1
        if mines > max_bombs:
            mines = max_bombs

        min_bombs = 1
        if mines < min_bombs:
            mines = min_bombs

        self.size = size
        self.board = Board(size, mines, tile_size)
        self.tile_size = tile_size
        self.board_size = (size[0] * tile_size, size[1] * tile_size)
