# -*- coding: utf-8 -*-
"""Test yourself on statistics"""

__copyright__ = 'Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved'
from collections import namedtuple


# NEW(28) USR(0) highlights
NTD = namedtuple('NTD', 'name text tags')
# pylint: disable=line-too-long
NTS = [
    # https://www.mathsisfun.com/combinatorics/combinations-permutations.html
    NTD._make(['Combination and order', "When the order doesn't matter, it is a Combination"]),
    NTD._make(['Combination without replacement',
               ("Order doesn't matter: ([1, 2, 3], 2) -> (1, 2) (1, 3) (2, 3)\n"
                "from itertools import combinations\n"
                "for p in combinations([1, 2, 3], repeat=2):")]),
    NTD._make(['Combination with replacement',
               ("Order doesn't matter: ([1, 2, 3], 2) -> (1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3)\n"
                "from itertools import combinations_with_replacement\n"
                "for p in combinations_with_replacement([1, 2, 3], repeat=2):")]),
    NTD._make(['Permutation and order', "When the order DOES Matter, it is a Permutation. P for Position"]),
    NTD._make(['Cartesian Product',
               ("[1, 2, 3] X [1, 2, 3] = (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)\n\n"
                "import itertools\nfor p in itertools.product([1, 2, 3], repeat=2")]),

]

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
