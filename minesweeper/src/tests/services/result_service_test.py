import unittest

from entities.result import Result
from entities.difficulty import Difficulty

from services.result_service import ResultService


class FakeResultRepository:
    def __init__(self):
        self.results = []

    def find_all(self):
        return self.results

    def save_result(self, result):
        self.results.append(result)

    def delete_all(self):
        self.results = []


class TestResultService(unittest.TestCase):
    def setUp(self):
        self.result_service = ResultService(FakeResultRepository())
        self.result_easy = Result(
            won=True,
            time=10000,
            difficulty=Difficulty.EASY
        )
        self.result_medium = Result(
            won=False,
            time=20000,
            difficulty=Difficulty.MEDIUM
        )
        self.result_hard = Result(
            won=True,
            time=100000,
            difficulty=Difficulty.HARD
        )

    def test_saving_result(self):
        self.result_service.save_result(self.result_easy)
        results = self.result_service.get_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].difficulty, Difficulty.EASY)
        self.assertEqual(results[0].won, True)
        self.assertEqual(results[0].time, 10000)

    def test_getting_stats(self):
        self.result_service.save_result(self.result_easy)
        self.result_service.save_result(self.result_medium)
        self.result_service.save_result(self.result_hard)

        stats = self.result_service.get_stats()

        self.assertEqual(stats["total_games"], 3)
        self.assertEqual(stats["total_wins"], 2)
        self.assertEqual(stats["total_losses"], 1)
        self.assertAlmostEqual(stats["winrate"], 2/3*100, places=2)
        self.assertEqual(stats["best_result_easy"].difficulty, Difficulty.EASY)
        self.assertEqual(stats["best_result_medium"], None)
        self.assertEqual(stats["best_result_hard"].difficulty, Difficulty.HARD)
