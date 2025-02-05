import random
import itertools
import numpy as np
from anytree import Node, RenderTree


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def convert_binary_array_to_int(binary_array):
        return int("".join([str(b) for b in binary_array]), 2)

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
    def __init__(self, default_base_two, name=None, is_9x9=False):
        """

        :param default_base_two: A two-dimensional base-2 numpy array.
        :param name: A name (optional).
        """

        self.name = name
        self.base_two = default_base_two
        # self.base_ten = [Utils.convert_binary_array_to_int(row) for row in self.base_two]
        self.height = len(self.base_two)
        self.width = len(self.base_two[0])

        # determine this bitboard's 9x9 bitboards, but only if it isn't already a 9x9
        if not is_9x9:
            self.base_two_9x9s = self._get_base_two_9x9s()

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        s = f"patch {self.name}\n"

        for row in self.base_two:
            s += "".join([str(r) for r in row.tolist()]).replace('0', '░').replace("1", "▓") + "\n"

        return s

    def _get_base_two_9x9s(self):
        """
        Generates all 9x9 bitboards that this one can fit into (base two).
        """

        nine_by_nines = []

        height_offset = 9 - self.height
        width_offset = 9 - self.width

        for i in range(0, height_offset + 1):
            for j in range(0, width_offset + 1):
                new_bitboard = []

                # apply height offset first
                for k in range(0, i):
                    new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                # insert real data, using width offset
                for row in self.base_two:
                    new_row = row.tolist()

                    for l in range(0, j):
                        new_row.insert(0, 0)

                    while len(new_row) < 9:
                        new_row.append(0)

                    new_bitboard.append(new_row)

                # insert remaining empty rows
                while len(new_bitboard) < 9:
                    new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                nine_by_nines.append(
                    Bitboard(
                        default_base_two=np.array(new_bitboard),
                        name=f"{self.name}O({i},{j})",
                        is_9x9=True
                    )
                )

        return nine_by_nines

    @property
    def is_full(self):
        """
        A bitboard is "full" if it only contains 1s.
        """

        return all([cell == 1 for row in self.base_two for cell in row])


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

        self.bitboards = self._get_bitboards()  # i.e. each of the patch's possible rotations / orientations

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        return str(self.bitboards[0])

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

    def get_valid_board_placements(self, board):
        """

        :param board:
        :type board: Board
        :return:
        """

        valid_9x9s = []

        possible_9x9s = [n for b in self.bitboards for n in b.base_two_9x9s]

        for pnn in possible_9x9s:
            new_9x9 = np.bitwise_and(board.bitboard.base_two, pnn.base_two)

            if not any(cell == 1 for row in new_9x9 for cell in row):
                valid_9x9s.append(pnn)

        return valid_9x9s


class Board:

    def __init__(self, bitboard=None):
        self.bitboard = bitboard if bitboard is not None else Bitboard(
            default_base_two=np.array([
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]),
            name="Board"
        )

        self.acquired_patches = ()

    def __str__(self):
        return str(self.bitboard)

    def place_patch(self, valid_9x9_bitboard):
        """
        Overlays a presumably valid 9x9 patch bitboard on the existing board.

        :param valid_9x9_bitboard: A 9x9 patch bitboard.
        """

        new_bitboard = []

        for i in range(0, 9):
            new_bitboard.append(np.bitwise_or(self.bitboard.base_two[i], valid_9x9_bitboard.base_two[i]))

        self.bitboard = Bitboard(default_base_two=np.array(new_bitboard), name="Board", is_9x9=True)

    @property
    def buttons(self):
        return sum([patch.buttons for patch in self.acquired_patches])

    @property
    def filled_squares_count(self):
        return sum([bin(row).count("1") for row in self.bitboard])

    # todo: test
    def has_seven_by_seven_bonus(self):
        """
        Returns True if any of the 9x9 board's constituent 7x7 boards are full.
        """

        for i in range(0, 3):
            for j in range(0, 3):
                seven_by_seven = Bitboard(
                    name="temp",
                    default_base_two=np.array([row[0+j:7+j] for row in self.bitboard[0+i:7+i]])
                )

                if seven_by_seven.is_full:
                    return True

        return False


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

