#!/usr/bin/env python3
"""Section A) The Paired t-Test; the Confidence Interval Component"""
# https://stackoverflow.com/questions/28242593/correct-way-to-obtain-confidence-interval-with-scipy
#
# http://ocw.jhsph.edu/courses/StatisticalReasoning1/PDFs/2009/BiostatisticsLecture6.pdf

# An Introduction to Hypothesis Testing: The Paired t-Test"""
# John McGready, Johns Hopkins University

from collections import namedtuple
import numpy as np
import scipy.stats
import scipy.stats as stats
from pkgstat.mcgready.fncs import get_proportion
from pkgstat.mcgready.fncs import cii
from pkgstat.mcgready.fncs import ztest


def main():
    # Of the 180 women randomized to AZT group, 13 gave birth to
    # children who tested positive for HIV within 18 months of birth
    azt = get_proportion(13, 180)
    cii(180, 13)
    # Of the 183 women randomized to the placebo group, 40 gave
    # birth to children who tested positive for HIV within 18 months of birth
    placebo = get_proportion(40, 183)
    cii(183, 40)
    # Lecture 3. Example 1
    cii(481, 219)

    print(ztest(13, 180, 40, 183))
    print(ztest(10000, 20000, 4000, 20000))

    #model_org1 = cii(2000, 1000)
    #model_org0 = cii(2000,  400)

    ##cii(100, 123.4, 13.7)

####     data = [
####         [13, 167],  # 180
####         [40, 143],  # 183
####     ]
#### 
####     data_hiv = [
####         # Exposre
####         # AZT  Placebo  # Outcome
####         [13,       40], # YES HIV Transmission
####         [167,     143], #  NO HIV Transmission
####     ]
####     oddsratio, pvalue = stats.fisher_exact(data)
####     print(oddsratio, pvalue)
#### 
#### def cii(total, affected):
####     """Confidence interval"""
####     nto = cx.namedtuple('NtCII', 'Obs Mean SE CI95')
####     obs = total
####     mean = 1.0*affected/total
####     stderr = 


if __name__ == '__main__':
    main()
