import unittest
import random
from engine.pieces import Pieces


class EngineTests(unittest.TestCase):

    all_pieces = Pieces.pieces

    @staticmethod
    def test_get_orientations():
        p = EngineTests.all_pieces[1]

        for o in p.orientations:
            print(p.print_orientation(o))

    @staticmethod
    @unittest.skip
    def test_print_piece():
        random_pieces = random.sample(EngineTests.all_pieces, 10)

        for p in random_pieces:
            print(p)
