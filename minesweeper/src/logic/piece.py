class Piece:
    def __init__(self, is_bomb: bool, location: tuple):
        self.is_bomb = is_bomb
        self.clicked = False
        self.flagged = False
        self.location = location

    def reveal(self):
        if not self.flagged:
            self.clicked = True

    def flag_piece(self):
        if not self.clicked:
            self.flagged = not self.flagged
