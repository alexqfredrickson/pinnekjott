import numpy as np
from engine.models.piece import Piece


class Pieces:
    pieces = [
        Piece(
            base_orientation=np.array([[0, 1, 1, 0], [1, 1, 1, 1]]),
            buttons=2,
            turns=4,
            cost=7,
            name="A"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 1], [0, 1, 1], [1, 1, 0]]),
            buttons=3,
            turns=6,
            cost=8,
            name="B"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0]]),
            buttons=1,
            turns=3,
            cost=5,
            name="C"
        ),
        Piece(
            base_orientation=np.array([[0, 1], [1, 1], [1, 1], [1, 0]]),
            buttons=0,
            turns=2,
            cost=4,
            name="D"
        ),
        Piece(
            base_orientation=np.array([[1, 1], [1, 1]]),
            buttons=2,
            turns=5,
            cost=6,
            name="E"
        ),
        Piece(
            base_orientation=np.array([[1, 0, 1], [1, 1, 1]]),
            buttons=0,
            turns=2,
            cost=1,
            name="F"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 0], [1, 1, 1]]),
            buttons=0,
            turns=2,
            cost=2,
            name="G"
        ),
        Piece(
            base_orientation=np.array([[1, 1, 1, 1]]),
            buttons=1,
            turns=3,
            cost=3,
            name="H"
        ),
        Piece(
            base_orientation=np.array([[1, 0, 0], [1, 1, 0], [0, 1, 1]]),
            buttons=3,
            turns=4,
            cost=10,
            name="I"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
            buttons=2,
            turns=2,
            cost=7,
            name="J"
        ),
        Piece(
            base_orientation=np.array(
                [
                    [0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0]
                ]
            ),
            buttons=1,
            turns=4,
            cost=1,
            name="K"
        ),
        Piece(
            base_orientation=np.array([[0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0]]),
            buttons=0,
            turns=2,
            cost=1,
            name="L"
        ),
        Piece(
            base_orientation=np.array([[0, 0, 1, 0], [1, 1, 1, 1]]),
            buttons=1,
            turns=4,
            cost=3,
            name="M"
        ),
        Piece(
            base_orientation=np.array([[0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]]),
            buttons=1,
            turns=3,
            cost=0,
            name="N"
        ),
        Piece(
            base_orientation=np.array([[1, 0, 0, 1], [1, 1, 1, 1]]),
            buttons=1,
            turns=5,
            cost=1,
            name="O"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 0], [0, 1, 0], [1, 1, 1]]),
            buttons=2,
            turns=5,
            cost=5,
            name="P"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 0], [0, 1, 1], [1, 1, 0], [0, 1, 0]]),
            buttons=0,
            turns=1,
            cost=2,
            name="Q"
        ),
        Piece(
            base_orientation=np.array([[1, 1, 1, 1, 1]]),
            buttons=1,
            turns=1,
            cost=7,
            name="R"
        ),
        Piece(
            base_orientation=np.array([[1, 0, 0, 0], [1, 1, 1, 1]]),
            buttons=2,
            turns=3,
            cost=10,
            name="S"
        ),
        Piece(
            base_orientation=np.array([[0, 0, 1], [1, 1, 1]]),
            buttons=1,
            turns=2,
            cost=4,
            name="T"
        ),
        Piece(
            base_orientation=np.array([[0, 0, 1], [1, 1, 1]]),
            buttons=2,
            turns=6,
            cost=4,
            name="U"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 1], [1, 1, 0], [0, 1, 1]]),
            buttons=2,
            turns=6,
            cost=3,
            name="V"
        ),
        Piece(
            base_orientation=np.array([[0, 1], [1, 1], [1, 1]]),
            buttons=0,
            turns=2,
            cost=2,
            name="W"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 1], [1, 1, 0]]),
            buttons=3,
            turns=6,
            cost=7,
            name="X"
        ),
        Piece(
            base_orientation=np.array([[1, 0, 1], [1, 1, 1], [1, 0, 1]]),
            buttons=0,
            turns=3,
            cost=2,
            name="Y"
        ),
        Piece(
            base_orientation=np.array([[1, 1], [1, 1], [0, 1], [0, 1]]),
            buttons=3,
            turns=5,
            cost=10,
            name="Z"
        ),
        Piece(
            base_orientation=np.array([[0, 1], [1, 1]]),
            buttons=0,
            turns=1,
            cost=3,
            name="AA"
        ),
        Piece(
            base_orientation=np.array([[0, 1], [1, 1], [1, 0]]),
            buttons=1,
            turns=2,
            cost=3,
            name="BB"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 1, 1], [1, 1, 0, 0]]),
            buttons=1,
            turns=3,
            cost=2,
            name="CC"
        ),
        Piece(
            base_orientation=np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
            buttons=2,
            turns=4,
            cost=5,
            name="DD"
        ),
        Piece(
            base_orientation=np.array([[0, 1], [1, 1]]),
            buttons=0,
            turns=3,
            cost=1,
            name="EE"
        ),
        Piece(
            base_orientation=np.array([[1, 1]]),
            buttons=0,
            turns=1,
            cost=2,
            name="FF"
        ),
        Piece(
            base_orientation=np.array([[1, 1, 1]]),
            buttons=0,
            turns=2,
            cost=2,
            name="GG"
        )
    ]


