import unittest
from entities.result import Result
from entities.difficulty import Difficulty
from repositories.result_repository import result_repository


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        result_repository.delete_all()

    def test_save_result(self):
        result = Result(
            difficulty=Difficulty.EASY, won=True, time=12000, date='2025-01-01')
        result_repository.save_result(result)
        results = result_repository.find_all()

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].difficulty, Difficulty.EASY)
        self.assertEqual(results[0].won, True)
        self.assertEqual(results[0].time, 12)  # seconds
        self.assertEqual(results[0].date, '2025-01-01')

    def test_find_all_results(self):
        result_repository.save_result(Result(
            difficulty=Difficulty.HARD, won=True, time=120000))
        result_repository.save_result(Result(
            difficulty=Difficulty.MEDIUM, won=False, time=15000))

        results = result_repository.find_all()

        self.assertEqual(len(results), 2)
