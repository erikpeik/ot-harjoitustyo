from entities.difficulty import Difficulty
from entities.result import Result
from repositories.result_repository import (
    result_repository as default_result_repository)


class ResultService:
    """Luokka, joka hallitsee pelin tuloksia ja niiden käsittelyä.
    """

    def __init__(self, result_repository=default_result_repository):
        self._result_repository = result_repository

    def get_results(self) -> list[Result]:
        """Hakee kaikki tulokset tietokannasta.

        Returns:
            list[Result]: Kaikki tulokset tietokannasta.
        """

        return self._result_repository.find_all()

    def get_results_by_difficulty(self, difficulty: Difficulty) -> list[Result]:
        """Hakee kaikki tulokset tietokannasta vaikeusasteen mukaan.

        Args:
            difficulty (Difficulty): Vaikeusaste, jonka mukaan tulokset haetaan.

        Returns:
            list[Result]: Tulokset, jotka vastaavat annettua vaikeusastetta.
        """
        return self._result_repository.find_by_difficulty(difficulty)

    def save_result(self, result: Result):
        """Tallentaa tuloksen tietokantaan.

        Args:
            result (Result): Tallennettava tulos.
        """
        self._result_repository.save_result(result)

    def get_stats(self) -> dict:
        """Laskee pelin tilastot ja palauttaa ne sanakirjana.

        Returns:
            dict: Pelin tilastot, kuten voitot, häviöt ja voittoprosentti.
        """
        results = self.get_results()
        for result in results:
            print(result.difficulty, result.won, result.time, result.date)

        total_games = len(results)
        total_wins = len([result for result in results if result.won])
        total_losses = len([result for result in results if not result.won])
        winrate = (total_wins / total_games) * 100 if total_games else 0

        best_easy_result = min(
            (result for result in results if result.difficulty ==
                Difficulty.EASY and result.won),
            key=lambda x: x.time, default=None
        )
        best_medium_result = min(
            (result for result in results if result.difficulty ==
                Difficulty.MEDIUM and result.won),
            key=lambda x: x.time, default=None
        )
        best_hard_result = min(
            (result for result in results if result.difficulty ==
                Difficulty.HARD and result.won),
            key=lambda x: x.time, default=None
        )

        return {
            "total_games": total_games,
            "total_wins": total_wins,
            "total_losses": total_losses,
            "winrate": winrate,
            "best_result_won": best_easy_result,
            "best_result_medium": best_medium_result,
            "best_result_hard": best_hard_result,
        }


result_service = ResultService()
