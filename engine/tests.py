import unittest
import random
from models.piece import Piece, Board
from engine.pieces import Pieces


class EngineTests(unittest.TestCase):

    all_pieces = Pieces.pieces
    board = Board()

    def test_print_piece(self):
        for p in self.all_pieces:
            print(p)

    def test_print_board(self):
        self.board.print_board()

    def test_place_piece_on_board(self):
        random_piece = random.sample(self.all_pieces, k=1)[0]
        random_piece_orientation = random.sample(random_piece.all_possible_orientations, k=1)[0]
        self.board.place_piece_on_board((4, 5), random_piece_orientation)
