import random
import itertools
import numpy as np
from anytree import Node, RenderTree


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def convert_binary_array_to_int(binary_array):
        return int("".join([b for b in binary_array]), 2)

    @staticmethod
    def convert_int_to_binary_array(integer):
        binary_str = bin(integer)[2:]  # remove the '0b' prefix
        binary_array = [int(bit) for bit in binary_str]
        return binary_array

    @staticmethod
    def shift_binary_array_right(binary_array):
        # simply prepend a 0, and remove the last item
        for row in binary_array:
            row.prepend(0)
            row.pop()

    @staticmethod
    def shift_binary_array_left(binary_array):
        # simply pop the first item in each row, and append a 0
        for row in binary_array:
            row.pop(0)
            row.append(0)


class Bitboard:
    def __init__(self, default_base_two, name=None):
        """

        :param default_base_two: A two-dimensional base-2 numpy array.
        :param name: A name (optional).
        """

        self.name = name
        self.base_two = default_base_two
        self.base_ten = Utils.convert_binary_array_to_int(self.base_two)
        self.height = len(self.base_two)
        self.width = len(self.base_two[0])

        self.base_two_9x9s = self._get_base_two_9x9s()

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        s = f"patch {self.name}\n"

        for row in self.base_two:
            s += (format(row, f"0{int.bit_length(max(self.base_two))}b")  # bit-based string formatting lol
                  .replace('0', '.')
                  .replace("1", "▓") + "\n")

        return s

    def _get_base_two_9x9s(self):
        """
        Generates all 9x9 bitboards that this one can fit into (base two).
        """

        nine_by_nines = set()

        height_offset = 9 - self.height
        width_offset = 9 - self.width

        for i in range(0, height_offset):
            for j in range(0, width_offset):
                new_bitboard = []

                # apply height offset first
                for k in range(0, i):
                    new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                # insert real data, using width offset
                for row in self.base_two:
                    new_row = row.copy()

                    for l in range(0, j):
                        new_row.prepend(0)

                    while len(new_row) < 9:
                        new_row.append(0)

                # insert remaining empty rows
                while len(new_bitboard) < 9:
                    new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                nine_by_nines.add(new_bitboard)

        return nine_by_nines


class BasePolyominoes:
    """
    The base set of polyominoes that encircle the board.
    """

    def __init__(self):
        self.base_polyominoes = [
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1, 0],
                    [1, 1, 1, 1]]
                ),
                buttons=2,
                time_cost=4,
                button_cost=7,
                name="Pa"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1],
                    [0, 1, 1],
                    [1, 1, 0]]
                ),
                buttons=3,
                time_cost=6,
                button_cost=8,
                name="Pb"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1, 0],
                    [1, 1, 1, 1],
                    [0, 1, 1, 0]]
                ),
                buttons=1,
                time_cost=3,
                button_cost=5,
                name="Pc"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1],
                    [1, 1],
                    [1, 1],
                    [1, 0]]
                ),
                buttons=0,
                time_cost=2,
                button_cost=4,
                name="Pd"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1],
                    [1, 1]]
                ),
                buttons=2,
                time_cost=5,
                button_cost=6,
                name="Pe"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 0, 1],
                    [1, 1, 1]]
                ),
                buttons=0,
                time_cost=2,
                button_cost=1,
                name="Pf"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 0],
                    [1, 1, 1]]
                ),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="Pg"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1, 1, 1]]
                ),
                buttons=1,
                time_cost=3,
                button_cost=3,
                name="Ph"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1]]
                ),
                buttons=3,
                time_cost=4,
                button_cost=10,
                name="Pi"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [1, 1, 1]]
                ),
                buttons=2,
                time_cost=2,
                button_cost=7,
                name="Pj"
            ),
            Patch(
                default_bitboard=np.array(
                    [
                        [0, 0, 1, 0, 0],
                        [1, 1, 1, 1, 1],
                        [0, 0, 1, 0, 0]
                    ]
                ),
                buttons=1,
                time_cost=4,
                button_cost=1,
                name="Pk"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 0, 0, 1],
                    [1, 1, 1, 1],
                    [1, 0, 0, 0]
                ]),
                buttons=0,
                time_cost=2,
                button_cost=1,
                name="Pl"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 0, 1, 0],
                    [1, 1, 1, 1]
                ]),
                buttons=1,
                time_cost=4,
                button_cost=3,
                name="Pm"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 0, 1, 0],
                    [1, 1, 1, 1],
                    [0, 0, 1, 0]
                ]),
                buttons=1,
                time_cost=3,
                button_cost=0,
                name="Pn"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 0, 0, 1],
                    [1, 1, 1, 1]
                ]),
                buttons=1,
                time_cost=5,
                button_cost=1,
                name="Po"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 0],
                    [0, 1, 0],
                    [1, 1, 1]
                ]),
                buttons=2,
                time_cost=5,
                button_cost=5,
                name="Pp"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 0],
                    [0, 1, 1],
                    [1, 1, 0],
                    [0, 1, 0]
                ]),
                buttons=0,
                time_cost=1,
                button_cost=2,
                name="Pq"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1, 1, 1, 1]
                ]),
                buttons=1,
                time_cost=1,
                button_cost=7,
                name="Pr"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 0, 0, 0],
                    [1, 1, 1, 1]
                ]),
                buttons=2,
                time_cost=3,
                button_cost=10,
                name="Ps"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 0, 1],
                    [1, 1, 1]
                ]),
                buttons=1,
                time_cost=2,
                button_cost=4,
                name="Pt"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 0, 1],
                    [1, 1, 1]
                ]),
                buttons=2,
                time_cost=6,
                button_cost=4,
                name="Pu"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1],
                    [1, 1, 0],
                    [0, 1, 1]
                ]),
                buttons=2,
                time_cost=6,
                button_cost=3,
                name="Pv"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1],
                    [1, 1],
                    [1, 1]
                ]),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="Pw"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1],
                    [1, 1, 0]
                ]),
                buttons=3,
                time_cost=6,
                button_cost=7,
                name="Px"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 0, 1],
                    [1, 1, 1],
                    [1, 0, 1]
                ]),
                buttons=0,
                time_cost=3,
                button_cost=2,
                name="Py"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1],
                    [1, 1],
                    [0, 1],
                    [0, 1]
                ]),
                buttons=3,
                time_cost=5,
                button_cost=10,
                name="Pz"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1],
                    [1, 1]
                ]),
                buttons=0,
                time_cost=1,
                button_cost=3,
                name="Paa"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1],
                    [1, 1],
                    [1, 0]
                ]),
                buttons=1,
                time_cost=2,
                button_cost=3,
                name="Pbb"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 1, 1],
                    [1, 1, 0, 0]
                ]),
                buttons=1,
                time_cost=3,
                button_cost=2,
                name="Pcc"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]]
                ),
                buttons=2,
                time_cost=4,
                button_cost=5,
                name="Pdd"
            ),
            Patch(
                default_bitboard=np.array([
                    [0, 1],
                    [1, 1]]
                ),
                buttons=0,
                time_cost=3,
                button_cost=1,
                name="Pee"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1]]
                ),
                buttons=0,
                time_cost=1,
                button_cost=2,
                name="Pff"
            ),
            Patch(
                default_bitboard=np.array([
                    [1, 1, 1]]
                ),
                buttons=0,
                time_cost=2,
                button_cost=2,
                name="Pgg"
            )
        ]


class Monominos:
    """
    The 1x1 polyominos obtained by advancing through the track.
    """

    def __init__(self):
        self.monomino = Patch(
            default_bitboard=np.array([[1]]),
            buttons=0,
            time_cost=0,
            button_cost=0,
            name="Phh"
        )


class Patch:
    """
    A Patchwork patch (or 'patch') is a polyomino, with extra baggage.
    """

    def __init__(self, default_bitboard, buttons, time_cost, button_cost, name):
        """
        :param default_bitboard: A list of two-dimensional base-2 numpy arrays.
        :type default_bitboard: list of np.array()
        :param buttons: The amount of buttons depicted on the patch.
        :type buttons: int
        :param time_cost: The amount of "hops" performed when this patch is purchased.
        :type time_cost: int
        :param button_cost: The cost of this patch (in buttons).
        :type button_cost: int
        :param name: A friendly name for this patch.
        :type name: str
        """

        self.default_bitboard = default_bitboard
        self.buttons = buttons
        self.time_cost = time_cost
        self.button_cost = button_cost
        self.name = name

        self.bitboards = self._get_bitboards()

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        return str(self.default_bitboard)

    def _get_bitboards(self):

        bitboards = []

        for i in range(0, 4):  # get unflipped rotations

            bitboard = np.rot90(self.default_bitboard, k=i)

            if not any([b for b in bitboards if np.array_equal(b.base_two, bitboard)]):
                bitboards.append(Bitboard(default_base_two=bitboard, name=f"{self.name}R{i}F0"))

        flipped_base_orientation = np.flip(self.default_bitboard, axis=1)  # get flipped rotations

        for i in range(0, 4):
            bitboard = np.rot90(flipped_base_orientation, k=i)

            if not any([b for b in bitboards if np.array_equal(b.base_two, bitboard)]):
                bitboards.append(Bitboard(default_base_two=bitboard, name=f"{self.name}R{i}F1"))

        return bitboards

    def is_affordable_by_player(self, player):
        return player.buttons >= self.button_cost


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
        self.acquired_patches = ()

    def __str__(self):
        s = ""

        for row in self.bitboard:
            s += format(row, "09b") + "\n"

        return s

    def place_patch(self, board_position, patch_orientation):
        """
        Places a patch on the board.

        The patch's squares represent a "bitboard mask".

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
        :param patch_orientation: One of a patch's possible orientations.
        :type patch_orientation: list of list of int
        """

        top_offset = board_position[0]
        left_offset = board_position[1]

        target_rows = range(top_offset, top_offset + len(patch_orientation))

        orientation_length = max([int.bit_length(x) for x in patch_orientation])

        j = 0

        for i in target_rows:
            self.bitboard[i] = self.bitboard[i] | (patch_orientation[j] << (9 - left_offset - orientation_length))
            j += 1

    @property
    def buttons(self):
        return sum([patch.buttons for patch in self.acquired_patches])

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

        # initialize and randomize patches
        self.starting_position = [p for p in BasePolyominoes().base_polyominoes]
        random.shuffle(self.starting_position)
        self.patches = itertools.cycle(self.starting_position)  # pull with `next(pool)`

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
            # four base decisions: hop, pick first patch, pick second patch, or pick third patch
            # each patch pick requires placement
            decision_node = Node("foo", player=self.active_player, hop=False, patch=None, patch_placement_position=None, parent=base_node)
            self.populate_decision_tree(decision_node, depth)
        else:
            for pre, fill, node in RenderTree(self.decision_tree):
                # print("%s%s" % (pre, node.name))
                pass  # todo


