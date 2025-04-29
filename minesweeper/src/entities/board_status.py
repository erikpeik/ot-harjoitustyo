from enum import Enum


class BoardStatus(Enum):
    """Boardin tila enum-luokka, joka määrittelee pelin eri tilat.
    """
    NOT_STARTED = 0
    RUNNING = 1
    GAME_OVER = 2
    WON = 3
