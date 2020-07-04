#!/usr/bin/env python3
"""Math from Lecture done in Python"""

from scipy import stats
from scipy.stats import norm


def test_lec2():
    """Math from Lecture done in Python"""
    bps = [89, 99, 101, 101, 103, 103, 104, 105, 106, 106]
    print(stats.describe(bps))
    slide24()

def slide24():
    # Slide 24) Example 1: Blood Pressure in Males
    # For z=0.5, roughly 69% of observations fall below .5 SDs from he mean
    print(norm.cdf(.5))
    # 0.6914624612740131


if __name__ == '__main__':
    test_lec2()
