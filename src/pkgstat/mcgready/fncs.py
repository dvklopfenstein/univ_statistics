# -*- coding: utf-8 -*-
"""Functions from John McGready's Statistics course"""

__copyright__ = 'Copyright (C) 2020-present DV Klopfenstein. All rights reserved'

from collections import namedtuple
import math
import scipy
from scipy.stats import norm

# Statistical Reasoning I by John McGready at Johns Hopkins University

### Lecture 3:

#### The Central Limit Theorem (CLT)
#      is a powerful mathematical tool that gives several useful results
#      - The sampling distribution of sample means based on all samples
#        of same size n is approximately normal, regardless of the
#        distribution of the original (individual level) data in the
#        population/samples
#      - The mean of all sample means in the sampling distribution is
#        the true mean of the population from which the samples were
#        taken, µ
#      - Standard deviation in the sample means of size n is equal to :
#        this is often called the standard error of the sample mean and
#        sometimes written as SE(x_bar)

####   Notes on Confidence Intervals (p20)
#      * Are all CIs 95%?
#        - No
#        - It is the most commonly used
#        - A 99% CI is wider
#        - A 90% CI is narrower
#      * To change level of confidence adjust number of SE added and subtracted from x_bar
#        - For a 99% CI, you need ± 2.6 SE
#        - For a 95% CI, you need ± 2 SE
#        - For a 90% CI, you need ± 1.65 SE

##  Module 3:  Comparing Two Groups and Hypothesis Testing

### Lecture 5: Comparing Means among Two (or More) Independent Populations 
#     * CIs for mean difference between two independent populations
#     * Two sample t-test
#     * Non-parametric alternative, Mann Whitney (FYI, optional)
#     * Comparing means amongst more than two independent populations: ANOVA

### Lecture 6: Comparing Proportions between Two Independent Populations
#     * Using CIs for difference in proportions between two independent populations
#     * Large sample methods for comparing proportions between two populations
#       - Normal method
#       - Chi-squared test
#     * Fisher’s exact test
#     * Relative risk 

def get_proportion(num, tot):
    """Proportion of observed proportions 6a p8"""
    return float(num)/tot

def cii(tot, mean, stddev=None):
    """Confidence intervals for proportions 6a p9"""
    nto = namedtuple('NtCII', 'Obs Mean SE CI95')
    num = 1.7211883421013974
    num = 2.0
    if stddev is None:
        # Lecture 3 Example 1
        proportion = get_proportion(mean, tot)
        proportion = round(proportion, 7)
        print(proportion)
        # Standard error of the sample proportion, SE(p_hat)
        stderr = math.sqrt(proportion*(1-proportion)/tot)
        mean = proportion
    else:
        stderr = stddev/math.sqrt(tot)
    stderr = round(stderr, 7)
    print(stderr)
    ciival = round(num*stderr, 7)
    #stderr = .019294
    #mean = get_proportion(num, tot)
    #### print((mean - .0390137)/stderr)
    print(mean - ciival, mean + ciival)

# https://ipython-books.github.io/72-getting-started-with-statistical-hypothesis-testing-a-simple-z-test/#:~:text=The%20z-test%20is%20the%20normalized%20version%20of%20x,%C2%AF%20%E2%88%92%20q%29%20n%20q%20%281%20%E2%88%92%20q%29
def ztest(yes0, tot0, yes1, tot1):
    """Get p-value using Z-score"""
    prop0 = yes0/tot0
    prop1 = yes1/tot1
    print('PROPS', prop0, prop1, prop0-prop1)
    pn0 = prop0*(1 - prop0)/tot0
    pn1 = prop1*(1 - prop1)/tot1
    print('SE(p0 - p1)', math.sqrt(pn0 + pn1))
    zscore = (prop0 - prop1)/math.sqrt(pn0 + pn1)
    print('ZSCORE', zscore)
    # https://stackoverflow.com/questions/3496656/convert-z-score-z-value-standard-score-to-p-value-for-normal-distribution-in
    p_values = scipy.stats.norm.sf(abs(zscore))*2
    print('PVAL', p_values)


# Copyright (C) 2020-present DV Klopfenstein. All rights reserved
