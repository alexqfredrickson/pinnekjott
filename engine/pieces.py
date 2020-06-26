import numpy as np
from engine.models.piece import Piece


class Pieces:
    pieces = [
        Piece(
            squares=np.array([[False, True, True, False], [True, True, True, True]]),
            buttons=2,
            turns=4,
            cost=7
        ),
        Piece(
            squares=np.array([[False, True, True], [False, True, True], [True, True, False]]),
            buttons=3,
            turns=6,
            cost=8
        ),
        Piece(
            squares=np.array([[False, True, True, False], [True, True, True, True], [False, True, True, False]]),
            buttons=1,
            turns=3,
            cost=5
        ),
        Piece(
            squares=np.array([[False, True], [True, True], [True, True], [True, False]]),
            buttons=0,
            turns=2,
            cost=4
        ),
        Piece(
            squares=np.array([[True, True], [True, True]]),
            buttons=2,
            turns=5,
            cost=6
        ),
        Piece(
            squares=np.array([[True, False, True], [True, True, True]]),
            buttons=0,
            turns=2,
            cost=1
        ),
        Piece(
            squares=np.array([[False, True, False], [True, True, True]]),
            buttons=0,
            turns=2,
            cost=2
        ),
        Piece(
            squares=np.array([[True, True, True, True]]),
            buttons=1,
            turns=3,
            cost=3
        ),
        Piece(
            squares=np.array([[True, False, False], [True, True, False], [False, True, True]]),
            buttons=3,
            turns=4,
            cost=10
        ),
        Piece(
            squares=np.array([[False, True, False], [False, True, False], [False, True, False], [True, True, True]]),
            buttons=2,
            turns=2,
            cost=7
        ),
        Piece(
            squares=np.array(
                [
                    [False, False, True, False, False],
                    [True, True, True, True, True],
                    [False, False, True, False, False]
                ]
            ),
            buttons=1,
            turns=4,
            cost=1
        ),
        Piece(
            squares=np.array([[False, False, False, True], [True, True, True, True], [True, False, False, False]]),
            buttons=0,
            turns=2,
            cost=1
        ),
        Piece(
            squares=np.array([[False, False, True, False], [True, True, True, True]]),
            buttons=1,
            turns=4,
            cost=3
        ),
        Piece(
            squares=np.array([[False, False, True, False], [True, True, True, True], [False, False, True, False]]),
            buttons=1,
            turns=3,
            cost=0
        ),
        Piece(
            squares=np.array([[True, False, False, True], [True, True, True, True]]),
            buttons=1,
            turns=5,
            cost=1
        ),
        Piece(
            squares=np.array([[False, True, False], [False, True, False], [True, True, True]]),
            buttons=2,
            turns=5,
            cost=5
        ),
        Piece(
            squares=np.array([[False, True, False], [False, True, True], [True, True, False], [False, True, False]]),
            buttons=0,
            turns=1,
            cost=2
        ),
        Piece(
            squares=np.array([[True, True, True, True, True]]),
            buttons=1,
            turns=1,
            cost=7
        ),
        Piece(
            squares=np.array([[True, False, False, False], [True, True, True, True]]),
            buttons=2,
            turns=3,
            cost=10
        ),
        Piece(
            squares=np.array([[False, False, True], [True, True, True]]),
            buttons=1,
            turns=2,
            cost=4
        ),
        Piece(
            squares=np.array([[False, False, True], [True, True, True]]),
            buttons=2,
            turns=6,
            cost=4
        ),
        Piece(
            squares=np.array([[False, True, True], [True, True, False], [False, True, True]]),
            buttons=2,
            turns=6,
            cost=3
        ),
        Piece(
            squares=np.array([[False, True], [True, True], [True, True]]),
            buttons=0,
            turns=2,
            cost=2
        ),
        Piece(
            squares=np.array([[False, True, True], [True, True, False]]),
            buttons=3,
            turns=6,
            cost=7
        ),
        Piece(
            squares=np.array([[True, False, True], [True, True, True], [True, False, True]]),
            buttons=0,
            turns=3,
            cost=2
        ),
        Piece(
            squares=np.array([[True, True], [True, True], [False, True], [False, True]]),
            buttons=3,
            turns=5,
            cost=10
        ),
        Piece(
            squares=np.array([[False, True], [True, True]]),
            buttons=0,
            turns=1,
            cost=3
        ),
        Piece(
            squares=np.array([[False, True], [True, True], [True, False]]),
            buttons=1,
            turns=2,
            cost=3
        ),
        Piece(
            squares=np.array([[False, True, True, True], [True, True, False, False]]),
            buttons=1,
            turns=3,
            cost=2
        ),
        Piece(
            squares=np.array([[False, True, False], [True, True, True], [False, True, False]]),
            buttons=2,
            turns=4,
            cost=5
        ),
        Piece(
            squares=np.array([[False, True], [True, True]]),
            buttons=0,
            turns=3,
            cost=1
        ),
        Piece(
            squares=np.array([[True, True]]),
            buttons=0,
            turns=1,
            cost=2
        ),
        Piece(
            squares=np.array([[True, True, True]]),
            buttons=0,
            turns=2,
            cost=2
        )
    ]


