#!/usr/bin/env python3
"""Section A) The Paired t-Test; the Confidence Interval Component"""
# The CI approach allows us to create a range of possible values for mu
# using data from a single, impoerfect (paired) sample.
#
# ocw.jhsph.edu/courses/StatisticalReasoning1/PDFs/2009/BiostatisticsLecture4.pdf

# An Introduction to Hypothesis Testing: The Paired t-Test"""
# John McGready, Johns Hopkins University

from collections import namedtuple
import numpy as np
import scipy.stats

def main():
    """Section A) The Paired t-Test; the Confidence Interval Component"""
    ntobj = namedtuple('NtOC', 'BP_before_OC BP_after_OC')
    nts = [
        ntobj._make([115, 128]),  # 1.
        ntobj._make([112, 115]),  # 2.
        ntobj._make([107, 106]),  # 3.
        ntobj._make([119, 128]),  # 4.
        ntobj._make([115, 122]),  # 5.
        ntobj._make([138, 145]),  # 6.
        ntobj._make([126, 132]),  # 7.
        ntobj._make([105, 109]),  # 8.
        ntobj._make([104, 102]),  # 9.
        ntobj._make([115, 117]),  # 10.

    ]
    num_pt = len(nts)
    x_before, x_after = zip(*[(nt.BP_before_OC, nt.BP_after_OC) for nt in nts])
    x_diff = np.array(x_after) - np.array(x_before)
    print(x_diff)
    xbar_before = sum(x_before)/num_pt
    xbar_after = sum(x_after)/num_pt
    xbar_diff = xbar_after - xbar_before
    print(xbar_before, xbar_after, xbar_diff)

    # The sample standard deviation(s) of the differences is s_diff = 4.6
    sd_sample = np.sqrt(sum([(nt.BP_after_OC - nt.BP_before_OC - xbar_diff)**2 for nt in nts])/(num_pt - 1))
    print(sd_sample)
    print(scipy.stats.sem(x_diff))

    # In a population of women who use oral contraceptives,
    # is the average (expected) change in blood pressure (after-before) 0 or not?


if __name__ == '__main__':
    main()
