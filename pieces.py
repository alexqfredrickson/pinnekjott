import numpy as np


class Piece:
    def __init__(self, buttons, name, turns, sqaures):
        self.squares = sqaures
        self.name = name
        self.buttons = buttons
        self.turns = turns

    @property
    def is_chiral(self):
        pass


pieces = {
    Piece(
        np.array([
    ]
        )
}