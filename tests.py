import unittest
import random
from pfen.pfen import PFEN
from pinnekjott.models import Board, BasePolyominoes, Game, Player, Bitboard
import numpy as np


class EngineTests(unittest.TestCase):

    alice = Player(name="Alice")
    bob = Player(name="Bob")

    all_patches = BasePolyominoes().base_polyominoes

    board = Board()
    pfen = PFEN()

    @unittest.skip
    def test_print_pieces(self):
        for p in self.all_patches:
            print(p)

    @unittest.skip
    def test_print_piece_bitboards(self):
        random_piece = random.sample(self.all_patches, k=1)[0]

        for b in random_piece.bitboards:
            print(b)

    @unittest.skip
    def test_print_board(self):
        print(self.board)

    @unittest.skip
    def test_patch_has_valid_9x9s(self):
        random_piece = random.sample(self.all_patches, k=1)[0]

        for b in random_piece.bitboards:
            assert len(b.base_two_9x9s) > 0

    @unittest.skip
    def test_get_valid_9x9s(self):
        random_patch = random.sample(self.all_patches, k=1)[0]

        valid_9x9s = random_patch.get_valid_board_placements(Board())

        for v in valid_9x9s:
            print(v)

    @unittest.skip
    def test_place_patch(self):
        board = Board(
            bitboard=Bitboard(
                np.array([
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                ]),
                name="Board",
                is_9x9=True
            )
        )

        for i in range(0, 50):
            random_patch = random.sample(self.all_patches, k=1)[0]
            random_valid_placements = random_patch.get_valid_board_placements(board=board)
            try:
                random_valid_placement = random.sample([b for b in random_valid_placements], k=1)[0]
                print(random_valid_placement)
                board.place_patch(random_valid_placement)
                print(board)
            except ValueError as ve:
                print("FAILED TO FIND VALID PLACEMENT FOR PATCH:")
                print(random_patch)
                print(board)
                break

    @unittest.skip
    def test_print_starting_position(self):
        pinnekjott = Game(self.alice, self.bob)
        print(PFEN.get_starting_position_as_pfen(pinnekjott))

    @unittest.skip
    def test_start_engine(self):
        pinnekjott = Game(self.alice, self.bob)
        pinnekjott.start()
