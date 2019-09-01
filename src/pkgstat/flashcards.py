# -*- coding: utf-8 -*-
"""Test yourself on statistics"""

__copyright__ = 'Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved'
from collections import namedtuple


# NEW(28) USR(0) highlights
NTD = namedtuple('NTD', 'name text tags')
# pylint: disable=line-too-long
NTS = [
    # https://www.mathsisfun.com/combinatorics/combinations-permutations.html
    NTD._make(['Combination and order', "When the order doesn't matter, it is a Combination", ('combo',)]),

    NTD._make(['Combination without replacement',
               ("Order doesn't matter: combinations('ABCD', 2) -> AB AC AD BC BD CD\n"
                "from itertools import combinations\n"
                "for p in combinations([1, 2, 3], repeat=2):"),
               ('combo',)]),

    NTD._make(['Combination with replacement',
               ("Order doesn't matter: combinations_with_replacement('ABCD', 2) -> AA AB AC AD BB BC BD CC CD DD\n"
                "from itertools import combinations_with_replacement\n"
                "for p in combinations_with_replacement([1, 2, 3], r=2):"),
               ('combo',)]),

    NTD._make(['Permutation and order',
               ("When the order DOES Matter, it is a Permutation. P for Position\n"
                "Order matters: permutations('ABCD', 2) -> AB AC AD BA BC BD CA CB CD DA DB DC\n"),
               ('combo',)]),

    NTD._make(['Cartesian Product',
               ("ABCD x ABCD: product('ABCD', repeat=2) -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD\n"
                "import itertools\nfor p in itertools.product([1, 2, 3], repeat=2"),
               ("combo",)]),

]

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
