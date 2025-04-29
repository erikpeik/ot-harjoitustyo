from entities.difficulty import Difficulty


class Result:
    def __init__(self, time: int, difficulty: Difficulty, date: str):
        self.time = time
        self.difficulty = difficulty
        self.date = date
