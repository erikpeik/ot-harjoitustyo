import unittest
from logic.board import Board
from logic.board_status import BoardStatus


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board((9, 9), 10, 32, (0, 0))
        self.test_board = Board((9, 9), 10, 32, (0, 0))
        self.test_board.board[3][3].is_bomb = True
        self.test_board.board[3][4].is_bomb = True
        self.test_board.board[3][5].is_bomb = True
        self.test_board.board[4][3].is_bomb = True

    def test_bomb_is_placed(self):
        self.board.place_bombs((0, 0))
        bomb_count = sum(
            piece.is_bomb for row in self.board.board for piece in row)
        self.assertEqual(bomb_count, self.board.mine_count)

    def test_get_board_returns_board(self):
        board = self.board.get_board()
        self.assertEqual(board, self.board.board)

    def test_calculate_adjacent_bombs(self):
        piece = self.test_board.get_board()[4][4]
        adjacent_bombs = self.test_board.calculate_adjacent_bombs(piece)

        self.assertEqual(adjacent_bombs, 4)

    def test_has_started(self):
        self.board.status = BoardStatus.NOT_STARTED
        self.assertFalse(self.board.has_started())
        self.board.status = BoardStatus.RUNNING
        self.assertTrue(self.board.has_started())

    def test_end_game(self):
        self.board.status = BoardStatus.RUNNING
        self.board.end_game()
        self.assertEqual(self.board.status, BoardStatus.GAME_OVER)

    def test_check_win_condition(self):
        self.assertFalse(self.test_board.check_win())
        for row in self.test_board.get_board():
            for piece in row:
                if not piece.is_bomb:
                    piece.clicked = True
        self.assertTrue(self.test_board.check_win())
