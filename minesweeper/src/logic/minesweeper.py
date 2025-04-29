from logic.board import Board
from entities.difficulty import Difficulty


class Minesweeper:
    def __init__(self, difficulty: Difficulty, tile_size=32):
        size = (0, 0)
        mines = 0

        if difficulty == Difficulty.EASY:
            size = (9, 9)
            mines = 10
        elif difficulty == Difficulty.MEDIUM:
            size = (16, 16)
            mines = 40
        elif difficulty == Difficulty.HARD:
            size = (30, 16)
            mines = 99

        self.size = size

        self.tile_size = tile_size
        self.board_size = (size[0] * tile_size, size[1] * tile_size)
        self.frame_size = (
            self.board_size[0] + 16 * 2,
            self.board_size[1] + 16 + 46 + 16 * 4 + 30,
        )
        self.board_offset = (16, 46 + 16 * 4 + 30)
        self.board = Board(size, mines,
                           tile_size=tile_size,
                           board_offset=self.board_offset,
                           difficulty=difficulty)
        self.running = True

    def reset_game(self):
        self.board.reset_board()
        self.running = True
