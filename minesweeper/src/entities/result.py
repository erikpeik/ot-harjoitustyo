from datetime import datetime
from entities.difficulty import Difficulty


class Result:
    """Luokka pelin tulokselle.
    """

    def __init__(self,
                 difficulty: Difficulty,
                 *,
                 date: str = datetime.now().isoformat(),
                 time: int = 0,
                 won: bool = False,
                 result_id: int = None
                 ):
        """Luokka pelin tulokselle.

        Args:
            difficulty (Difficulty): Vaikeustaso.
            date (str, optional): Päivämäärä. Defaults to datetime.now().isoformat().
            time (int, optional): Pelin kesto. Defaults to 0.
            won (bool, optional): Onko voitettu. Defaults to False.
            result_id (int, optional): Tuloksen ID. Defaults to None.
        """
        self.id = result_id
        self.time = time
        self.difficulty = difficulty
        self.date = date
        self.won = won
