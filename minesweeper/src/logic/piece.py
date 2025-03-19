class Piece:
    def __init__(self, isBomb: bool):
        self.isBomb = isBomb
        self.clicked = False
        self.flagged = False
