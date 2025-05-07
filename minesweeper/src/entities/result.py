from datetime import datetime
from entities.difficulty import Difficulty


class Result:
    def __init__(self,
                 difficulty: Difficulty,
                 *,
                 date: str = datetime.now().isoformat(),
                 time: int = 0,
                 won: bool = False,
                 result_id: int = None
                 ):
        self.id = result_id
        self.time = time
        self.difficulty = difficulty
        self.date = date
        self.won = won
