import random
import itertools
import numpy as np
from anytree import Node, RenderTree


class GamePieces:
    def __init__(self):
        self.pieces = [
            Piece(
                base_orientation=np.array([[0, 1, 1, 0], [1, 1, 1, 1]]),
                buttons=2,
                time_cost=4,
                button_cost=7,
                name="A"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 1], [0, 1, 1], [1, 1, 0]]),
                buttons=3,
                time_cost=6,
                button_cost=8,
                name="B"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0]]),
                buttons=1,
                time_cost=3,
                button_cost=5,
                name="C"
            ),
            Piece(
                base_orientation=np.array([[0, 1], [1, 1], [1, 1], [1, 0]]),
                buttons=0,
                time_cost=2,
                button_cost=4,
                name="D"
            ),
            Piece(
                base_orientation=np.array([[1, 1], [1, 1]]),
                buttons=2,
                time_cost=5,
                button_cost=6,
                name="E"
            ),
            Piece(
                base_orientation=np.array([[1, 0, 1], [1, 1, 1]]),
                buttons=0,
                time_cost=2,
                button_cost=1,
                name="F"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 0], [1, 1, 1]]),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="G"
            ),
            Piece(
                base_orientation=np.array([[1, 1, 1, 1]]),
                buttons=1,
                time_cost=3,
                button_cost=3,
                name="H"
            ),
            Piece(
                base_orientation=np.array([[1, 0, 0], [1, 1, 0], [0, 1, 1]]),
                buttons=3,
                time_cost=4,
                button_cost=10,
                name="I"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
                buttons=2,
                time_cost=2,
                button_cost=7,
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
                time_cost=4,
                button_cost=1,
                name="K"
            ),
            Piece(
                base_orientation=np.array([[0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0]]),
                buttons=0,
                time_cost=2,
                button_cost=1,
                name="L"
            ),
            Piece(
                base_orientation=np.array([[0, 0, 1, 0], [1, 1, 1, 1]]),
                buttons=1,
                time_cost=4,
                button_cost=3,
                name="M"
            ),
            Piece(
                base_orientation=np.array([[0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]]),
                buttons=1,
                time_cost=3,
                button_cost=0,
                name="N"
            ),
            Piece(
                base_orientation=np.array([[1, 0, 0, 1], [1, 1, 1, 1]]),
                buttons=1,
                time_cost=5,
                button_cost=1,
                name="O"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 0], [0, 1, 0], [1, 1, 1]]),
                buttons=2,
                time_cost=5,
                button_cost=5,
                name="P"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 0], [0, 1, 1], [1, 1, 0], [0, 1, 0]]),
                buttons=0,
                time_cost=1,
                button_cost=2,
                name="Q"
            ),
            Piece(
                base_orientation=np.array([[1, 1, 1, 1, 1]]),
                buttons=1,
                time_cost=1,
                button_cost=7,
                name="R"
            ),
            Piece(
                base_orientation=np.array([[1, 0, 0, 0], [1, 1, 1, 1]]),
                buttons=2,
                time_cost=3,
                button_cost=10,
                name="S"
            ),
            Piece(
                base_orientation=np.array([[0, 0, 1], [1, 1, 1]]),
                buttons=1,
                time_cost=2,
                button_cost=4,
                name="T"
            ),
            Piece(
                base_orientation=np.array([[0, 0, 1], [1, 1, 1]]),
                buttons=2,
                time_cost=6,
                button_cost=4,
                name="U"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 1], [1, 1, 0], [0, 1, 1]]),
                buttons=2,
                time_cost=6,
                button_cost=3,
                name="V"
            ),
            Piece(
                base_orientation=np.array([[0, 1], [1, 1], [1, 1]]),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="W"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 1], [1, 1, 0]]),
                buttons=3,
                time_cost=6,
                button_cost=7,
                name="X"
            ),
            Piece(
                base_orientation=np.array([[1, 0, 1], [1, 1, 1], [1, 0, 1]]),
                buttons=0,
                time_cost=3,
                button_cost=2,
                name="Y"
            ),
            Piece(
                base_orientation=np.array([[1, 1], [1, 1], [0, 1], [0, 1]]),
                buttons=3,
                time_cost=5,
                button_cost=10,
                name="Z"
            ),
            Piece(
                base_orientation=np.array([[0, 1], [1, 1]]),
                buttons=0,
                time_cost=1,
                button_cost=3,
                name="AA"
            ),
            Piece(
                base_orientation=np.array([[0, 1], [1, 1], [1, 0]]),
                buttons=1,
                time_cost=2,
                button_cost=3,
                name="BB"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 1, 1], [1, 1, 0, 0]]),
                buttons=1,
                time_cost=3,
                button_cost=2,
                name="CC"
            ),
            Piece(
                base_orientation=np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
                buttons=2,
                time_cost=4,
                button_cost=5,
                name="DD"
            ),
            Piece(
                base_orientation=np.array([[0, 1], [1, 1]]),
                buttons=0,
                time_cost=3,
                button_cost=1,
                name="EE"
            ),
            Piece(
                base_orientation=np.array([[1, 1]]),
                buttons=0,
                time_cost=1,
                button_cost=2,
                name="FF"
            ),
            Piece(
                base_orientation=np.array([[1, 1, 1]]),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="GG"
            )
        ]


class Piece:
    """
    A Patchwork piece.
    """

    def __init__(self, base_orientation, buttons, time_cost, button_cost, name):
        """

        :param base_orientation: A two-dimensional numpy array containing 0 or 1 values. This is used to create
                                 "bitboard masks", which can be rotated or flipped.
        :type base_orientation: list of list of int
        :param buttons: The amount of buttons depicted on the piece.
        :type buttons: int
        :param time_cost: The amount of "hops" performed when this piece is purchased.
        :type time_cost: int
        :param button_cost: The cost of this piece (in buttons).
        :type button_cost: int
        :param name: A friendly name for this piece.
        :type name: str
        """

        self.base_orientation = base_orientation
        self.buttons = buttons
        self.time_cost = time_cost
        self.button_cost = button_cost
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

            orientation = np.rot90(self.base_orientation, k=i)

            if not any([o for o in orientations if np.array_equal(o.bitboard_mask, orientation)]):
                orientations.append(PieceOrientation(name=f"{self.name}R{i}F0", bitboard_mask=orientation))

        # get flipped rotations
        flipped_base_orientation = np.flip(self.base_orientation, axis=1)

        for i in range(0, 4):
            orientation = np.rot90(flipped_base_orientation, k=i)

            if not any([o for o in orientations if np.array_equal(o.bitboard_mask, orientation)]):
                orientations.append(PieceOrientation(name=f"{self.name}R{i}F1", bitboard_mask=orientation))

        return orientations

    def is_affordable_by_player(self, player):
        return player.buttons >= self.button_cost


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
        self.acquired_pieces = ()

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

        # print(self.bitboard)
        # print(piece_orientation)

        top_offset = board_position[0]
        left_offset = board_position[1]

        target_rows = range(top_offset, top_offset + len(piece_orientation))

        orientation_length = max([int.bit_length(x) for x in piece_orientation])

        j = 0

        for i in target_rows:
            self.bitboard[i] = self.bitboard[i] | (piece_orientation[j] << (9 - left_offset - orientation_length))
            j += 1

        # print(self.bitboard)

    @property
    def buttons(self):
        return sum([piece.buttons for piece in self.acquired_pieces])

    @property
    def filled_squares_count(self):
        return sum([bin(row).count("1") for row in self.bitboard])

    @property
    def has_seven_by_seven_bonus(self):
        return (
            all([row in (511, 510, 509, 508) for row in self.bitboard[0:7]]) or
            all([row in (511, 510, 509, 508) for row in self.bitboard[1:8]]) or
            all([row in (511, 510, 509, 508) for row in self.bitboard[2:9]]) or
            all([row in (254, 255, 510, 511) for row in self.bitboard[0:7]]) or
            all([row in (254, 255, 510, 511) for row in self.bitboard[1:8]]) or
            all([row in (254, 255, 510, 511) for row in self.bitboard[2:9]]) or
            all([row in (127, 255, 383, 511) for row in self.bitboard[0:7]]) or
            all([row in (127, 255, 383, 511) for row in self.bitboard[1:8]]) or
            all([row in (127, 255, 383, 511) for row in self.bitboard[2:9]])
        )


class Player:
    def __init__(self, name):
        self.name = name
        self.opponent = None

        self.board = Board()

        self.board_advancements = 0
        self.buttons = 0

    def can_hop_opponent(self):
        return self.board_advancements <= self.opponent.board_advancements

    @property
    def score(self):
        return (self.board.filled_squares_count * 2) + self.buttons + (7 if self.board.has_seven_by_seven_bonus else 0)


class Game:
    """
    The Patchwork engine!
    """

    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

        # ensure the players oppose one another
        self.player.opponent = self.opponent
        self.opponent.opponent = self.player

        # initialize and randomize pieces
        self.pieces = [p for p in GamePieces().pieces]
        random.shuffle(self.pieces)
        self.pieces = itertools.cycle(self.pieces)  # pull with `next(pool)`

        self.ply = 0
        self.max_board_advancements = 53
        self.max_depth = 5

        self.decision_tree = Node(name="Start", depth=0)

        self.final_decisions = []

    @property
    def is_over(self):
        return (self.player.board_advancements == self.max_board_advancements and
                self.opponent.board_advancements == self.max_board_advancements)

    @property
    def active_player(self):
        return self.player if self.player.board_advancements <= self.opponent.board_advancements else self.opponent

    @property
    def active_opponent(self):
        return self.opponent if self.active_player == self.player else self.player

    def start(self):
        while not self.is_over:
            self.populate_decision_tree(self.decision_tree, depth=0)

    def populate_decision_tree(self, base_node, depth):
        depth += 1

        if depth <= self.max_depth:
            # four base decisions: hop, pick first piece, pick second piece, or pick third piece
            # each piece pick requires placement
            decision_node = Node("foo", player=self.active_player, hop=False, piece=None, piece_placement_position=None, parent=base_node)
            self.populate_decision_tree(decision_node, depth)
        else:
            for pre, fill, node in RenderTree(self.decision_tree):
                print("%s%s" % (pre, node.name))


alice = Player(name="Alice")
bob = Player(name="Bob")

pinnekjott = Game(alice, bob)
pinnekjott.start()
