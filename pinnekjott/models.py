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


class Polyominoes:
    """
    The base set of polyominoes that encircle the board.
    """

    def __init__(self):
        self.polyominoes = [
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

        # the 1x1 polyomino obtained by advancing through the turn track
        self.monomino = Patch(
            default_bitboard=np.array([[1]]),
            buttons=0,
            time_cost=0,
            button_cost=0,
            name="Phh"
        )

        self.all_polyominoes = [p for p in self.polyominoes]
        self.all_polyominoes.append(self.monomino)


class Bitboard:
    def __init__(self, default_base_two, name=None):
        """

        :param default_base_two: A two-dimensional base-2 numpy array.
        :param name: A name (optional).
        """

        self.name = name
        self.base_two = default_base_two
        self.height = len(self.base_two)
        self.width = len(self.base_two[0])

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        s = f"patch {self.name}\n"

        for row in self.base_two:
            s += "".join([str(r) for r in row.tolist()]).replace('0', '░').replace("1", "▓") + "\n"

        return s

    @property
    def is_full(self):
        """
        A bitboard is "full" if it only contains 1s.
        """

        return all([cell == 1 for row in self.base_two for cell in row])


class PatchVariation:
    def __init__(self, name, parent_patch_name, bitboard):
        self.name = name
        self.base_patch_name = parent_patch_name
        self.bitboard = bitboard

        self.flipped = True if "F1" in self.name else False
        self.rotated = True if "R1" in self.name or "R2" in self.name or "R3" in self.name else False
        self.rotation_value = self._get_rotation_value()
        self.height_offset, self.width_offset = self._get_offsets()

    def _get_rotation_value(self):
        """
        The rotation value is 0 or None if the piece is not rotated. If the rotation value is 1, it is rotated 90
        degrees clockwise relative to its initial orientation. If 2, 180 degrees. If 3, 270 degrees.
        """

        if not self.rotated:
            return None

        if "R0" in self.name:
            return 0

        if "R1" in self.name:
            return 1

        if "R2" in self.name:
            return 2

        if "R3" in self.name:
            return 3

        return None

    def _get_offsets(self):
        """
        Returns height and width offsets.
        """

        if "O(" not in self.name:
            return None, None

        offset_index = self.name.find(",")

        return self.name[offset_index - 1], self.name[offset_index + 1]


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

        self.name = name
        self.default_bitboard = default_bitboard

        self.buttons = buttons
        self.time_cost = time_cost
        self.button_cost = button_cost

        self.variations = self._get_variations()  # i.e. each of the patch's possible rotations / orientations

    def __str__(self):
        """
        Prints a patch to the terminal.
        """

        return str(self.variations[0])

    def _get_variations(self):
        """
        Returns all bitboards representing this piece in flipped and rotated orientations.
        """

        patch_variations = []

        for flip_value in range(0, 2):

            # flip the default bitboard, if required
            bitboard = np.flip(self.default_bitboard, axis=1) if flip_value == 1 else self.default_bitboard

            for rotation_value in range(0, 4):

                # rotate the flipped-or-unflipped bitboard, if required
                bitboard = np.rot90(bitboard, k=rotation_value)

                # determine height and width of rotated/flippd bitboard
                height = len(bitboard)
                width = len(bitboard[0])

                for height_offset_value in range(0, 9 - height + 1):
                    for width_offset_value in range(0, 9 - width + 1):

                        # determine the unique name for this patch variation
                        variation_name = (f"{self.name}R{rotation_value}F{flip_value}"
                                          f"O({height_offset_value},{width_offset_value})")

                        # blow this up into a 9x9, applying height and width offsets as required
                        new_bitboard = []

                        for k in range(0, height_offset_value):
                            new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                        # insert real data, using width offset
                        for row in bitboard:
                            new_row = row.tolist()

                            for l in range(0, width_offset_value):
                                new_row.insert(0, 0)

                            while len(new_row) < 9:
                                new_row.append(0)

                            new_bitboard.append(new_row)

                        # insert remaining empty rows
                        while len(new_bitboard) < 9:
                            new_bitboard.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

                        try:
                            nine_by_nine_bitboard = np.array(new_bitboard)
                        except ValueError as e:
                            print(e)
                            exit(1)

                        if not any(
                                [pv for pv in patch_variations if np.array_equal(
                                pv.bitboard.base_two, nine_by_nine_bitboard
                        )]):
                            patch_variations.append(
                                PatchVariation(
                                    name=variation_name,
                                    parent_patch_name=self.name,
                                    bitboard=Bitboard(
                                        default_base_two=nine_by_nine_bitboard,
                                        name=variation_name
                                    )
                                )
                            )

        return patch_variations

    def is_affordable_by_player(self, player):
        return player.buttons >= self.button_cost

    def get_valid_board_placements(self, board):
        valid_patch_variations = []

        possible_patch_variations = [v.bitboard for v in self.variations]

        for ppv in possible_patch_variations:
            new_9x9 = np.bitwise_and(board.bitboard.base_two, ppv.base_two)

            if not any(cell == 1 for row in new_9x9 for cell in row):
                valid_patch_variations.append(ppv)

        return valid_patch_variations


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

        self.bitboard = Bitboard(default_base_two=np.array(new_bitboard), name="Board")

    @property
    def buttons(self):
        return sum([patch.buttons for patch in self.acquired_patches])

    @property
    def filled_squares_count(self):
        return sum([bin(row).count("1") for row in self.bitboard])

    # todo: test
    @property
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

    @property
    def island_count(self):
        """
        Determines the number of "islands" (i.e. contiguous '1's) on the board.

        Low island counts are generally an indication of efficient piece placement. If the board is completely full,
        you only have one island. This also means you've probably won the game. If the board looks like Indonesia,
        it's probably going to be hard to place pieces. Indonesia has 17,000 islands!

        This method decomposes the numpy array into a graph and implements breadth-first search.
        """

        pass
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


class Move:
    def __init__(self, player, patch):
        self.player = player
        self.patch = patch
        self.is_hop = True if not self.patch else False
        self.is_placement = True if not self.is_hop else False


class Game:
    """
    The Patchwork engine!
    """

    def __init__(self, player, opponent):
        self.patch_dictionary = self._initialize_patch_dictionary()
        self.player = player
        self.opponent = opponent

        # ensure the players oppose one another
        self.player.opponent = self.opponent
        self.opponent.opponent = self.player

        # initialize and randomize patches
        self.starting_position = [p for p in Polyominoes().polyominoes]
        random.shuffle(self.starting_position)

        self.patches = itertools.cycle(self.starting_position)  # pull with `next(pool)`

        self.ply = 0
        self.max_board_advancements = 53
        self.max_depth = 5

        self.decision_tree = Node(name="Start", depth=0)

        self.moves = []

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

    def _initialize_patch_dictionary(self):  # todo
        patch_dictionary = {}.fromkeys([p.name for p in Polyominoes().all_polyominoes])
        pass

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

