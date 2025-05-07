from database_connection import get_database_connection
from entities.difficulty import Difficulty
from entities.result import Result


def get_result_by_row(row):
    return Result(
        result_id=row["id"],
        won=row["won"] == 1,
        time=row["time"] / 1000,
        difficulty=Difficulty(row["difficulty"]),
        date=row["date"]
    ) if row else None


class ResultRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self) -> list[Result]:
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM results')
        rows = cursor.fetchall()
        return list(map(get_result_by_row, rows))

    def find_by_difficulty(self, difficulty: Difficulty):
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM results WHERE difficulty = ?', (difficulty.value,))
        rows = cursor.fetchall()
        return list(map(get_result_by_row, rows))

    def save_result(self, result: Result):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO results (difficulty, won, time, date) VALUES (?, ?, ?, ?)',
                       (result.difficulty.value,
                        1 if result.won else 0,
                        result.time,
                        result.date,
                        ))
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM results')
        self._connection.commit()


result_repository = ResultRepository(get_database_connection())
