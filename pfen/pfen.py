class PFEN:
    """
    PFEN is a string-notation that describes a position in a Patchwork game. For example:

    `PyPjPbPpPccPlPffPggPbbPaaPcPfPzPgPuPrPmPddPnPePsPvPtPeePaPxPiPkPoPdPqPhPw 1. Pbc1Pxf4 Pbc1Pxf4H ...`

    Game Concepts
    -------------
    - Each game has a "starting position", which refers to the ordering of the 33 randomized starting patches.
    - Players place one or more of these patches until they have advanced ahead of their opponent.
    - Players occasionally obtain and place 1x1 squares by virtue of advancing.
    - Players occasionally hop their opponent.

    PFEN Concepts
    -------------
    - Each "patch" is given an arbitrary name. Each leads with a capital `P` - for example: `Pff`.
    - 1x1 squares are uniformly named `Phh`.
    - The PFEN starts with a *starting position string*, which represents each piece, in (cyclical) order. This string
      terminates with a space
    - `1. ` denotes the first *move sequence* of each player.
    - A *move sequence* may contain *piece placements*, and/or *hops*.
    - A *hop* is denoted by a capital `H`, and may result in a 1x1 piece placement at some position. For example:
      `HPhhd5`.

      # todo: explain moves in greater detail

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

