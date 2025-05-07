import random
import pygame as pg

from logic.piece import Piece

from entities.difficulty import Difficulty
from entities.board_status import BoardStatus
from entities.result import Result

from services.result_service import result_service


class Board:
    """Pelilaudan luokka, joka hallitsee pelin logiikkaa.
    """

    def __init__(
        self,
        size: tuple,
        mines: int,
        *,
        tile_size: int,
        board_offset: tuple,
        difficulty: Difficulty
    ):
        """Luokan konstruktori, joka alustaa pelilaudan.

        Args:
            size (tuple): Pelilaudan koko (rivit, sarakkeet).
            mines (int): Miinojen määrä laudalla.
            tile_size (int): Laatan koko pikseleinä.
            board_offset (tuple): Pelilaudan sijainti näytöllä (x, y).
            difficulty (Difficulty): Pelin vaikeusaste.
        """
        self.size = size
        self.mine_count = mines
        self.board = self.empty_board()
        self.tile_size = tile_size
        self.status = BoardStatus.NOT_STARTED
        self.offset = board_offset
        self.time_ticks = [0, 0]
        self.difficulty = difficulty

    def empty_board(self) -> list[list[Piece]]:
        """Palauttaa tyhjät laudat, joissa ei ole miinoja.

        Returns:
            list[list[piece]]: Tyhjä pelilauta.
        """

        return [
            [Piece(False, (row, col)) for col in range(self.size[1])]
            for row in range(self.size[0])
        ]

    def place_bombs(self, position: tuple):
        """Asettaa miinat laudalle satunnaisesti.

        Args:
            position (tuple): Pelin aloituspaikka (x, y), johon miinoja ei aseteta.
        """
        mines_placed = 0
        while mines_placed < self.mine_count:
            row = random.randint(0, self.size[0] - 1)
            col = random.randint(0, self.size[1] - 1)
            piece = self.board[row][col]
            if not piece.is_bomb and not self.is_clicked_position(position, (row, col)):
                self.board[row][col] = Piece(True, (row, col))
                mines_placed += 1

    def is_clicked_position(self, position: tuple, rowcol: tuple) -> bool:
        """Tarkistaa, onko klikattu kohta laudalla, kyseisellä sijainnilla.

        Args:
            position (tuple): PyGame-ikkunan klikkauskoordinaatti (x, y).
            rowcol (tuple): Pelilaudan sijainti (rivi, sarake).

        Returns:
            bool: True, jos klikkauskohta on kyseisellä sijainnilla, muuten False.
        """
        x, y = (rowcol[0] * self.tile_size + self.offset[0],
                rowcol[1] * self.tile_size + self.offset[1])
        mx, my = position
        return x <= mx < x + self.tile_size and y <= my < y + self.tile_size

    def get_board(self):
        """Palauttaa pelilaudan.

        Returns:
            list[list[piece]]: Nykyisen pelilaudan
        """
        return self.board

    def calculate_adjacent_bombs(self, piece: Piece) -> int:
        """Laskee viereisten miinojen määrän annetussa ruudussa.

        Args:
            piece (Piece): Ruutu jossa lasketaan viereiset miinat.

        Returns:
            int: Viereisten miinojen määrä.
        """
        row, col = piece.location
        adjacent_bombs = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not (i == 0 and j == 0)
                    and self.board[row + i][col + j].is_bomb
                ):
                    adjacent_bombs += 1
        return adjacent_bombs

    def reveal_empty_tiles(self, piece: Piece):
        """Paljastaa tyhjät ruudut, kun klikkaat tyhjää ruutua.

        Tämä metodi paljastaa kaikki viereiset tyhjät ruudut, kun klikkaat tyhjää ruutua.

        Args:
            piece (Piece): Nykyinen ruutu
        """
        if piece.is_bomb:
            return

        if self.calculate_adjacent_bombs(piece) != 0:
            piece.reveal()
            return

        row, col = piece.location
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not self.board[row + i][col + j].clicked
                ):
                    self.board[row + i][col + j].reveal()
                    self.reveal_empty_tiles(self.board[row + i][col + j])

    def chord_piece(self, piece: Piece):
        """Paljastaa kaikki viereiset tyhjät ruudut, kun vasen ja oikea hiiren painike on painettu.

        Tämä metodi tarkistaa, onko viereisissä ruuduissa oikea määrä lippuja ja paljastaa ne.

        Args:
            piece (Piece): Klikattu ruutu
        """
        row, col = piece.location
        flagged_adjacent = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.size[0]
                    and 0 <= col + j < self.size[1]
                    and not (i == 0 and j == 0)
                    and self.board[row + i][col + j].flagged
                ):
                    flagged_adjacent += 1
        if flagged_adjacent != self.calculate_adjacent_bombs(piece):
            return
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if not (0 <= new_row < self.size[0] and 0 <= new_col < self.size[1]):
                    continue
                piece = self.board[row + i][col + j]
                if piece.clicked or piece.flagged:
                    continue
                piece.reveal()
                self.reveal_empty_tiles(self.board[row + i][col + j])
                if piece.is_bomb:
                    self.end_game()

    def end_game(self):
        """Asettaa pelin tilan pelin päättymiseksi ja ottaa ajan talteen.
        """
        self.status = BoardStatus.GAME_OVER
        self.time_ticks[1] = pg.time.get_ticks()

        result_service.save_result(
            Result(
                difficulty=self.difficulty,
                time=self.get_time_on_ticks(),
                won=False,
            )
        )

    def has_started(self):
        """Tarkistaa, onko peli aloitettu pelin tilasta.

        Returns:
            bool: False, jos peli ei ole aloitettu, muuten True.
        """
        return self.status != BoardStatus.NOT_STARTED

    def has_lost(self):
        """Tarkistaa, onko peli hävitty pelin tilasta.

        Returns:
            bool: True, jos peli on hävitty, muuten False.
        """
        return self.status == BoardStatus.GAME_OVER

    def has_won(self):
        """Tarkistaa, onko peli voitettu pelin tilasta.

        Returns:
            bool: True, jos peli on voitettu, muuten False.
        """
        return self.status == BoardStatus.WON

    def game_is_running(self):
        """Tarkistaa, onko peli käynnissä pelin tilasta.

        Returns:
            bool: True, jos peli on käynnissä, muuten False.
        """
        return self.status == BoardStatus.RUNNING

    def reset_board(self):
        """Uudelleenkäynnistää pelilaudan, asettaa pelin tilan ja asettaa ajan nollaksi.
        """
        self.board = self.empty_board()
        self.status = BoardStatus.NOT_STARTED
        self.time_ticks = [0, 0]

    def mines_left(self) -> int:
        """Miinojen määrä, joka on vielä asettamatta.

        Returns:
            int: Miinojen määrä, joka on vielä asettamatta.
        """
        if self.has_won():
            return 0
        return self.mine_count - sum(
            piece.flagged for row in self.board for piece in row
        )

    def check_win(self):
        """Tarkistaa, onko peli voitettu.

        Jos peli on voitettu, asetetaan pelin tila voitetuksi ja tallennetaan tulos.

        Returns:
            bool: True, jos peli on voitettu, muuten False.
        """
        for row in self.board:
            for piece in row:
                if not piece.is_bomb and not piece.clicked:
                    return False
        self.status = BoardStatus.WON
        self.time_ticks[1] = pg.time.get_ticks()

        result_service.save_result(
            Result(
                difficulty=self.difficulty,
                time=self.get_time_on_ticks(),
                won=True,
            )
        )

        return True

    def get_time_on_seconds(self) -> int:
        """Palauttaa pelin keston sekunteina.

        Returns:
            int: Pelin kesto sekunteina.
        """
        if self.time_ticks[0] == 0:
            return 0
        if not self.game_is_running():
            return (self.time_ticks[1] - self.time_ticks[0]) // 1000
        return (pg.time.get_ticks() - self.time_ticks[0]) // 1000

    def get_time_on_ticks(self) -> int:
        """Palauttaa pelin keston millisekunteina.

        Returns:
            int: Pelin kesto millisekunteina.
        """
        if self.time_ticks[0] == 0:
            return 0
        if not self.game_is_running():
            return self.time_ticks[1] - self.time_ticks[0]
        return pg.time.get_ticks() - self.time_ticks[0]
