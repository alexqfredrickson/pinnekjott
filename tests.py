import unittest
import random
from models import Board
from data import GamePieces


class EngineTests(unittest.TestCase):

    all_pieces = GamePieces().pieces
    board = Board()

    @unittest.skip
    def test_print_pieces(self):
        for p in self.all_pieces:
            print(p)

    @unittest.skip
    def test_print_piece_orientations(self):
        random_piece = random.sample(self.all_pieces, k=1)[0]

        for o in random_piece.orientations:
            print(o)

    @unittest.skip
    def test_print_board(self):
        print(self.board)

    @unittest.skip
    def test_place_piece_on_board(self):
        random_piece = random.sample(self.all_pieces, k=1)[0]
        random_piece_orientation = random.sample([o.bitboard_mask for o in random_piece.orientations], k=1)[0]
        self.board.place_piece_on_board((1, 1), random_piece_orientation)
