import unittest
import unittest.mock

from logic.minesweeper import Minesweeper
from entities.difficulty import Difficulty


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper(Difficulty.EASY)

    def test_reset_game_calls_reset_board(self):
        self.minesweeper.board.reset_board = unittest.mock.Mock()
        self.minesweeper.reset_game()
        self.minesweeper.board.reset_board.assert_called_once()
