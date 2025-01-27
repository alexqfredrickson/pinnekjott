class PFEN:
    """
    PFEN is a string-notation that describes a position in a Patchwork game. For example:

    `PyPjPbPpPccPlPffPggPbbPaaPcPfPzPgPuPrPmPddPnPePsPvPtPeePaPxPiPkPoPdPqPhPw 1. PbR0F0c1Pxf4 PcR0F0c1Pdf4H ...`

    Game Concepts
    -------------
    ⦾ Each game has a "starting position", which refers to the ordering of the 33 randomized starting patches.
    ⦾ Players place one or more of these patches until they have advanced ahead of their opponent.
    ⦾ Players occasionally obtain and place 1x1 squares by virtue of advancing.
    ⦾ Players occasionally hop their opponent.

    Starting Position
    -------------
    ⦾ Each patch is given a unique arbitrary name, leading with `P`. For example: `Pff`.
        ⦾ 1x1 squares are all called `Phh`.
    ⦾ The PFEN begins with a sequence of patch names representing the starting position.
        ⦾ It terminates with a single whitespace.

    Turns
    -----
    ⦾ Each turn is denoted by an integer. For example: `1. `.
    ⦾ Each turn has two *move sequences*.

    Move Sequences
    --------------
    ⦾ A player's move sequence consists of zero or more *piece placements*, and may end with a *hop*.

    Piece Placements
    ----------------
    ⦾ In the *piece placement* section, each patch is described with its rotations and flips, in a certain location.
        ⦾ Rotations are denoted by `R0`, `R1`, `R2`, or `R3`, depending on whether or not the patch is rotated 0, 90,
          180, or 270 degrees clockwise (respectively).
        ⦾ Flips are denoted by `F0` or `F1`, depending on whether or not the patch is flipped along its first axis
          (according to np.flip(axis=1)).
        ⦾ Placements are described in algebraic notation, where A1 refers to the top-left quadrant, and I9 refers to
          the bottom-right quadrant.
          ⦾ Placements are described as if the piece occupies its own NxM board, where N is the piece height and M
            is the piece width.

    ⦾ For example: PbR1F1c1 means the `Pb` piece is flipped, and then rotated 90 degrees clockwise, and then placed at
      `c1` (as if the piece was a rectangle).

    ⦾ A *hop* is denoted by a capital `H`, and may result in a 1x1 piece placement at some position. For example:
      `HPhhd5`.

    Other Notes
    -----------
    - There are 33! (8,683,317,618,811,886,495,518,194,401,280,000,000) possible starting positions. This makes the
      prospect of an opening book rather daunting.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_starting_position_as_pfen(game):
        return "".join([p.name for p in game.starting_position])

