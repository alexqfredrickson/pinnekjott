import numpy


class Piece:
    """
    A Patchwork piece.
    """

    def __init__(self, squares, buttons, turns, cost):
        """

        :param squares: A two-dimensional numpy array containing boolean values.
        :type squares: list of list of bool
        :param buttons: The amount of buttons depicted on the piece.
        :type buttons: int
        :param turns: The amount of "hops" performed when this piece is purchased.
        :type turns: int
        :param cost: The cost of this piece (in buttons).
        :type cost: int
        """

        self.squares = squares
        self.buttons = buttons
        self.turns = turns
        self.cost = cost

        self.orientations = self.get_orientations()

    def __str__(self):
        return self.print_piece(self.squares)

    @staticmethod
    def print_piece(arr):
        """
        Prints a piece to the terminal.

        :param arr: A two-dimensional array of boolean values.
        """

        s = ""

        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if arr[i][j]:
                    s += "▓"
                else:
                    s += " "

            s += "\n"

        return s

    def get_orientations(self):
        """
        Returns an array of a piece's possible rotated/flipped orientations.
        """

        orientations = []

        # get normal rotations
        for i in range(0, 4):
            orientations.append(numpy.rot90(self.squares, k=i))

        # get flipped rotations
        flipped_squares = numpy.flip(self.squares, axis=1)

        for i in range(0, 4):
            orientations.append(numpy.rot90(flipped_squares, k=i))

        # remove redundant orientations
        unique_orientations = []

        for i, o1 in enumerate(orientations):
            if not numpy.any([o2 for o2 in unique_orientations if numpy.array_equal(o1, o2)]):
                unique_orientations.append(o1)

        return unique_orientations
