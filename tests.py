import unittest
import random
from pfen.pfen import PFEN
from pinnekjott.models import Board, BasePolyominoes, Game, Player


class EngineTests(unittest.TestCase):

    alice = Player(name="Alice")
    bob = Player(name="Bob")

    all_pieces = BasePolyominoes().base_polyominoes

    board = Board()
    pfen = PFEN()

    @unittest.skip
    def test_print_pieces(self):
        for p in self.all_pieces:
            print(p)

    @unittest.skip
    def test_print_piece_bitboards(self):
        random_piece = random.sample(self.all_pieces, k=1)[0]

        for b in random_piece.bitboards:
            print(b)

    @unittest.skip
    def test_print_board(self):
        print(self.board)

    def test_place_patch(self):
        random_piece = random.sample(self.all_pieces, k=1)[0]
        random_piece_orientation = random.sample([b for b in random_piece.bitboards], k=1)[0]
        self.board.place_patch((1, 1), random_piece_orientation)

    @unittest.skip
    def test_print_starting_position(self):
        pinnekjott = Game(self.alice, self.bob)
        print(PFEN.get_starting_position_as_pfen(pinnekjott))

    @unittest.skip
    def test_start_engine(self):
        pinnekjott = Game(self.alice, self.bob)
        pinnekjott.start()
