from entities.difficulty import Difficulty
from repositories.result_repository import (
    result_repository as default_result_repository)


class ResultService:
    def __init__(self, result_repository=default_result_repository):
        self._result_repository = result_repository

    def get_results(self):
        return self._result_repository.find_all()

    def get_results_by_difficulty(self, difficulty: Difficulty):
        return self._result_repository.find_by_difficulty(difficulty)

    def save_result(self, run_time: int, difficulty: Difficulty):
        self._result_repository.save_result(run_time, difficulty)


result_service = ResultService()
