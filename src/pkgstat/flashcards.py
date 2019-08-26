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
    NTD._make(['Permutation and order', "When the order DOES Matter, it is a Permutation. P for Position"]),

]

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
