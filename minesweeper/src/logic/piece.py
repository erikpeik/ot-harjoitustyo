class Piece:
    def __init__(self, is_bomb: bool):
        self.is_bomb = is_bomb
        self.clicked = False
        self.flagged = False
