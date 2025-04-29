class Piece:
    """Luokka, joka edustaa yksittäistä ruutua pelilaudalla.

    Tämä luokka sisältää tiedot sijainnista,
    onko ruutu pommi, onko se paljastettu ja onko se merkitty lipulla.
    """

    def __init__(self, is_bomb: bool, location: tuple):
        """Luokan konstruktori, joka alustaa ruudun tiedot.

        Args:
            is_bomb (bool): True, jos ruutu on pommi, muuten False.
            location (tuple): Ruutu sijainti (rivi, sarake) muodossa.
        """
        self.is_bomb = is_bomb
        self.clicked = False
        self.flagged = False
        self.location = location

    def reveal(self):
        """Paljastaa ruudun, jos se ei ole merkitty lipulla.
        """
        if not self.flagged:
            self.clicked = True

    def flag_piece(self):
        """Merkitsee ruudun lipulla, jos se ei ole paljastettu.
        """
        if not self.clicked:
            self.flagged = not self.flagged
