import numpy


class Piece:
    """
    A Patchwork piece.
    """

    def __init__(self, base_orientation, buttons, turns, cost, name):
        """

        :param base_orientation: A two-dimensional numpy array containing 0 or 1 values. This represents a
                                 "bitboard mask". Pieces can be rotated and flipped.
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

        self.all_possible_orientations = self.get_all_possible_orientations()

    def __str__(self):
        return self.print_piece(self.name, self.base_orientation)

    @staticmethod
    def print_piece(name, base_orientation):
        """
        Prints a piece to the terminal.

        :param base_orientation: A two-dimensional array of boolean values.
        """

        s = f"Piece {name}\n"

        for i in range(0, len(base_orientation)):
            for j in range(0, len(base_orientation[i])):
                if base_orientation[i][j]:
                    s += "▓"
                else:
                    s += "."

            s += "\n"

        return s

    def get_all_possible_orientations(self):
        """
        Returns an array of a piece's possible rotated/flipped orientations.
        """

        orientations = []

        # get normal rotations
        for i in range(0, 4):
            orientations.append(numpy.rot90(self.base_orientation, k=i))

        # get flipped rotations
        flipped_squares = numpy.flip(self.base_orientation, axis=1)

        for i in range(0, 4):
            orientations.append(numpy.rot90(flipped_squares, k=i))

        # remove redundant orientations
        unique_orientations = []

        for i, o1 in enumerate(orientations):
            if not numpy.any([o2 for o2 in unique_orientations if numpy.array_equal(o1, o2)]):
                unique_orientations.append(o1)

        return unique_orientations


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

    def print_board(self):
        """
        Prints a board to the terminal.
        """

        for row in self.bitboard:
            print("{0:{fill}9b}".format(row, fill='0'))

        print("")

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

        top_offset = board_position[0]
        left_offset = board_position[1]

        # convert piece orientation from big-endian binary array to integer
        piece_orientation_as_ints = [] >> (8 - left_offset)

        for row in piece_orientation:
            piece_orientation_as_ints.append(int(row, 2) << board_position)

        for i in range(0, 9):
            if i < top_offset:
                continue
            # self.bitboard[i] = self.bitboard[i] |

            # todo
            pass



