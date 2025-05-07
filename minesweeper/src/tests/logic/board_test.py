import unittest

from logic.board import Board
from entities.board_status import BoardStatus
from entities.difficulty import Difficulty


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board((9, 9), 10, tile_size=32, board_offset=(
            0, 0), difficulty=Difficulty.EASY)
        self.test_board = Board((9, 9), 10, tile_size=32, board_offset=(
            0, 0), difficulty=Difficulty.EASY)
        self.test_board.board[0][6].is_bomb = True
        self.test_board.board[1][1].is_bomb = True
        self.test_board.board[2][2].is_bomb = True
        self.test_board.board[3][7].is_bomb = True
        self.test_board.board[4][4].is_bomb = True
        self.test_board.board[6][2].is_bomb = True
        self.test_board.board[6][4].is_bomb = True
        self.test_board.board[6][8].is_bomb = True
        self.test_board.board[7][7].is_bomb = True
        self.test_board.board[8][3].is_bomb = True

    def test_bomb_is_placed(self):
        self.board.place_bombs((0, 0))
        bomb_count = sum(
            piece.is_bomb for row in self.board.board for piece in row)
        self.assertEqual(bomb_count, self.board.mine_count)

    def test_get_board_returns_board(self):
        board = self.board.get_board()
        self.assertEqual(board, self.board.board)

    def test_calculate_adjacent_bombs(self):
        board = Board((9, 9), 10, tile_size=32, board_offset=(
            0, 0), difficulty=Difficulty.EASY)

        board.board[3][3].is_bomb = True
        board.board[3][4].is_bomb = True
        board.board[3][5].is_bomb = True
        board.board[4][3].is_bomb = True

        piece = board.get_board()[4][4]
        adjacent_bombs = board.calculate_adjacent_bombs(piece)

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
        self.assertFalse(self.board.check_win())
        for row in self.board.get_board():
            for piece in row:
                if not piece.is_bomb:
                    piece.clicked = True
        self.assertTrue(self.board.check_win())

    def test_revealing_tiles(self):
        self.test_board.reveal_empty_tiles(self.test_board.get_board()[1][4])
        self.assertTrue(self.test_board.get_board()[0][4].clicked)
        self.assertTrue(self.test_board.get_board()[0][3].clicked)
        self.assertTrue(self.test_board.get_board()[2][4].clicked)
        self.assertTrue(self.test_board.get_board()[2][5].clicked)

    def test_chord_piece(self):
        self.test_board.get_board()[1][5].clicked = True
        self.test_board.get_board()[0][6].flagged = True
        self.test_board.chord_piece(self.test_board.get_board()[1][5])
        self.assertTrue(self.test_board.get_board()[0][5].clicked)
        self.assertTrue(self.test_board.get_board()[0][4].clicked)
        self.assertTrue(self.test_board.get_board()[1][4].clicked)
        self.assertTrue(self.test_board.get_board()[1][6].clicked)
        self.assertTrue(self.test_board.get_board()[2][5].clicked)
        self.assertTrue(self.test_board.get_board()[2][4].clicked)
        self.assertTrue(self.test_board.get_board()[2][6].clicked)
