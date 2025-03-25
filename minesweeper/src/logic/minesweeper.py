from logic.board import Board


class Minesweeper:
    def __init__(self, size=(30, 16), mines=99, tile_size=32):
        max_size = (30, 16)
        min_size = (9, 9)

        size = (
            min(max_size[0], max(min_size[0], size[0])),
            min(max_size[1], max(min_size[1], size[1])),
        )
        max_bombs = size[0] * size[1] - 1
        mines = min(mines, max_bombs)

        min_bombs = 1
        mines = max(mines, min_bombs)

        self.size = size

        self.tile_size = tile_size
        self.board_size = (size[0] * tile_size, size[1] * tile_size)
        self.frame_size = (
            self.board_size[0] + 16 * 2,
            self.board_size[1] + 16 + 46 + 16 * 4,
        )
        self.board_offset = (16, 46 + 16 * 4)
        self.board = Board(size, mines, tile_size, self.board_offset)
