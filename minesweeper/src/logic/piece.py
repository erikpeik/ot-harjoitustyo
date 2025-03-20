class Piece:
    def __init__(self, is_bomb: bool, location: tuple):
        self.is_bomb = is_bomb
        self.clicked = False
        self.flagged = False
        self.location = location

    def reveal(self):
        self.clicked = True
