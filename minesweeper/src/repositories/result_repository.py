from sqlite3 import Connection
from database_connection import get_database_connection
from entities.difficulty import Difficulty
from entities.result import Result


def get_result_by_row(row) -> Result:
    """Muodostaa Result-olion tietokannan rivistä.

    Args:
        row (Any): Tietokannan rivi, joka sisältää tuloksen tiedot.

    Returns:
        Result: Result-olio, joka sisältää tuloksen tiedot.
    """
    return Result(
        result_id=row["id"],
        won=row["won"] == 1,
        time=row["time"] / 1000,
        difficulty=Difficulty(row["difficulty"]),
        date=row["date"]
    ) if row else None


class ResultRepository:
    """Luokka, joka hallitsee tulosten tallentamista ja hakemista tietokannasta.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka alustaa tietokantayhteyden.

        Args:
            connection (Connection): Tietokantayhteys tulosten tallentamiseen ja hakemiseen.
        """
        self._connection: Connection = connection

    def find_all(self) -> list[Result]:
        """ Hakee kaikki tulokset tietokannasta.

        Returns:
            list[Result]: Kaikki tulokset tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM results')
        rows = cursor.fetchall()
        return list(map(get_result_by_row, rows))

    def find_by_difficulty(self, difficulty: Difficulty) -> list[Result]:
        """Hakee kaikki tulokset tietokannasta vaikeusasteen mukaan.

        Args:
            difficulty (Difficulty): Vaikeusaste, jonka mukaan tulokset haetaan.

        Returns:
            list[Result]: Tulokset, jotka vastaavat annettua vaikeusastetta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM results WHERE difficulty = ?', (difficulty.value,))
        rows = cursor.fetchall()
        return list(map(get_result_by_row, rows))

    def save_result(self, result: Result):
        """Tallentaa tuloksen tietokantaan.

        Args:
            result (Result): Tallennettava tulos.
        """
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO results (difficulty, won, time, date) VALUES (?, ?, ?, ?)',
                       (result.difficulty.value,
                        1 if result.won else 0,
                        result.time,
                        result.date,
                        ))
        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki tulokset tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM results')
        self._connection.commit()


result_repository = ResultRepository(get_database_connection())
