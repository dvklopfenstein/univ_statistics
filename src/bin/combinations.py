#!/usr/bin/env python3
"""Show conbinations, conbinations w/replacement, permutations, product"""

__copyright__ = 'Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved'

from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product


# pylint: disable=line-too-long
def main():
    """Demonstrate  combinatoric generators"""
    abc = 'ABC'
    print(abc)
    print('combinations       ', ' '.join([''.join(a) for a in combinations(abc, 2)]))
    print('combinations_w_repl', ' '.join([''.join(a) for a in combinations_with_replacement(abc, 2)]))
    print('permutations       ', ' '.join([''.join(a) for a in permutations(abc, 2)]))
    print('product            ', ' '.join([''.join(a) for a in product(abc, repeat=2)]))


if __name__ == '__main__':
    main()

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
