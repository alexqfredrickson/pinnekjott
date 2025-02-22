import unittest
import random
from pfen.pfen import PFEN
from pinnekjott.models import Board, Polyominoes, Game, Player, Bitboard
import numpy as np


class EngineTests(unittest.TestCase):

    alice = Player(name="Alice")
    bob = Player(name="Bob")

    all_polyominoes = Polyominoes().all_polyominoes

    pfen = PFEN()
    game = Game(alice, bob)

    @unittest.skip
    def test_noop(self):
        assert True

    @unittest.skip
    def test_print_patches(self):
        for p in self.all_polyominoes:
            print(p)

    @unittest.skip
    def test_print_patch_variations(self):
        random_patch = random.sample(self.all_polyominoes, k=1)[0]

        for b in random_patch.variations:
            print(b)

    @unittest.skip
    def test_print_board(self):
        print(self.alice.board)

    @unittest.skip
    def test_patch_has_valid_9x9s(self):
        random_patch = random.sample(self.all_polyominoes, k=1)[0]

        for v in random_patch.variations:
            assert len(v.bitboard.base_two_9x9s) > 0

    @unittest.skip
    def test_get_valid_9x9s(self):
        random_patch = random.sample(self.all_polyominoes, k=1)[0]

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
                name="Board"
            )
        )

        for i in range(0, 50):
            random_patch = random.sample(self.all_polyominoes, k=1)[0]
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
