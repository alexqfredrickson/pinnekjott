import numpy


class Piece:
    """
    A Patchwork piece.
    """

    def __init__(self, base_orientation, buttons, turns, cost, name):
        """

        :param base_orientation: A two-dimensional numpy array containing 0 or 1 values. This is used to create
                                 "bitboard masks", which can be rotated or flipped.
        :type base_orientation: list of list of int
        :param buttons: The amount of buttons depicted on the piece.
        :type buttons: int
        :param turns: The amount of "hops" performed when this piece is purchased.
        :type turns: int
        :param cost: The cost of this piece (in buttons).
        :type cost: int
        :param name: A friendly name for this piece.
        :type name: str
        """

        self.base_orientation = base_orientation
        self.buttons = buttons
        self.turns = turns
        self.cost = cost
        self.name = name

        self.orientations = self._get_possible_orientations()

    def __str__(self):
        """
        Prints a piece to the terminal.
        """

        s = f"Piece {self.name}\n"

        for i in range(0, len(self.base_orientation)):
            for j in range(0, len(self.base_orientation[i])):
                if self.base_orientation[i][j]:
                    s += "▓"
                else:
                    s += "."

            s += "\n"

        return s

    def _get_possible_orientations(self):
        """
        Returns an array of a piece's possible rotated/flipped orientations.
        """

        orientations = []

        # get normal rotations
        for i in range(0, 4):

            orientation = numpy.rot90(self.base_orientation, k=i)

            if not any([o for o in orientations if numpy.array_equal(o.bitboard_mask, orientation)]):
                orientations.append(PieceOrientation(name=f"{self.name}R{i}F0", bitboard_mask=orientation))

        # get flipped rotations
        flipped_base_orientation = numpy.flip(self.base_orientation, axis=1)

        for i in range(0, 4):
            orientation = numpy.rot90(flipped_base_orientation, k=i)

            if not any([o for o in orientations if numpy.array_equal(o.bitboard_mask, orientation)]):
                orientations.append(PieceOrientation(name=f"{self.name}R{i}F1", bitboard_mask=orientation))

        return orientations


class PieceOrientation:
    def __init__(self, name, bitboard_mask):
        self.name = name
        self.bitboard_mask = bitboard_mask

    def __str__(self):
        """
        Prints a piece to the terminal.
        """

        s = f"Piece {self.name}\n"

        for row in self.bitboard_mask:
            s += (format(row, f"0{int.bit_length(max(self.bitboard_mask))}b")  # bit-based string formatting lol
                  .replace('0', '.')
                  .replace("1", "▓") + "\n")

        return s


class Board:
    """
    A 9x9 board, represented as nine 9-bit integers, in big-endian binary form.

    This represents an empty board:              This represents a non-empty board:

    0:  000000000                                0: 000000000
    0:  000000000                                0: 000000000
    0:  000000000                                8: 000001000
    0:  000000000                               28: 000011100
    0:  000000000                                8: 000001000
    0:  000000000                                0: 000000000
    0:  000000000                                0: 000000000
    0:  000000000                                0: 000000000
    0:  000000000                                0: 000000000

    """

    def __init__(self):
        self.bitboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # each integer in the array represents a row, from top to bottom

    def __str__(self):
        s = ""

        for row in self.bitboard:
            s += format(row, "09b") + "\n"

        return s

    def place_piece_on_board(self, board_position, piece_orientation):
        """
        Places a piece on the board.

        The piece's squares represent a "bitboard mask".

        :param board_position: A tuple containing the offset distances from the top and left sides of the board (respectively).

        For example:

        (0,0)      X       X      X      X      X      X      X       X
          X        X       X      X      X      X      X    (1,7)     X
          X      (2,1)     X      X      X      X      X      X       X
          X        X       X      X      X      X      X      X       X
          X        X       X      X    (4,4)    X      X      X       X
          X        X       X      X      X      X      X      X       X
          X        X       X      X      X      X      X      X       X
          X        X       X      X      X      X      X      X       X
          X        X       X      X    (8,4)    X      X      X     (8,8)

        :type board_position: tuple
        :param piece_orientation: One of a piece's possible orientations.
        :type piece_orientation: list of list of int
        """

        print(self.bitboard)
        print(piece_orientation)

        top_offset = board_position[0]
        left_offset = board_position[1]

        target_rows = range(top_offset, top_offset + len(piece_orientation))

        orientation_length = max([int.bit_length(x) for x in piece_orientation])

        j = 0

        for i in target_rows:
            self.bitboard[i] = self.bitboard[i] | (piece_orientation[j] << (9 - left_offset - orientation_length))
            j += 1

        print(self.bitboard)

