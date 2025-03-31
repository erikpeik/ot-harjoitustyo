import unittest
from logic.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board((9, 9), 10, 32, (0, 0))
        self.board.place_bombs((16, 16))

    def test_bomb_is_placed(self):
        bomb_count = sum(piece.is_bomb for row in self.board.board for piece in row)
        self.assertEqual(bomb_count, self.board.mine_count)

    def test_get_board_returns_board(self):
        board = self.board.get_board()
        self.assertEqual(board, self.board.board)
