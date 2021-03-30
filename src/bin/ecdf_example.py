#!/usr/bin/env python3
"""Example plotting of ECDF"""
# https://stackoverflow.com/questions/15792552/numpy-scipy-equivalent-of-r-ecdfxx-function/37660583#37660583

# pylint: disable=wrong-import-position,line-too-long
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

def main():
    """Example plotting of empirical distribution (cumulative) function (ECDF)"""
    fout_png = 'ex_grades_ecdf.png'
    grades = (93.5, 93, 60.8, 94.5, 82, 87.5, 91.5, 99.5, 86, 93.5, 92.5, 78, 76, 69, 94.5,
              89.5, 92.8, 78, 65.5, 98, 98.5, 92.3, 95.5, 76, 91, 95, 61)
    print('GRADES:                                ', ' '.join(['{:4.1f}'.format(n) for n in sorted(grades)]))

    xvals, yvals = _ecdf_wrong(grades)
    plt.plot(xvals, yvals, label="wrong cumsum")
    xvals, yvals = _ecdf_correct(grades)
    plt.plot(xvals, yvals, label="handwritten", marker=">", markerfacecolor='none')
    cdf = ECDF(grades)
    plt.plot(cdf.x, cdf.y, label="statmodels", marker="<", markerfacecolor='none')
    plt.title('Good v Bad empirical distribution (cumulative) function (ECDF)')
    plt.xlabel('Grades')
    plt.legend(loc=2)
    plt.savefig(fout_png)
    print('  WROTE: {PNG}'.format(PNG=fout_png))

def _ecdf_wrong(data):
    xvals = np.sort(data) # need to be sorted
    numerator = np.cumsum(xvals)
    denominator = np.sum(xvals)
    yvals = numerator/denominator # normalize so sum == 1
    print('WRONG   PERCENTILE Y VALUE   NUMERATOR:', ' '.join(['{:4}'.format(n) for n in numerator]))
    print('WRONG   PERCENTILE Y VALUE DENOMINATOR:', denominator)
    return xvals, yvals

def _ecdf_correct(data):
    xvals = np.sort(data)
    num_xvals = len(xvals)
    # Y values are evenly spaced values within a given interval
    numerator = np.arange(1, num_xvals+1)
    denominator = float(num_xvals)
    print('CORRECT PERCENTILE Y VALUE   NUMERATOR:', ' '.join(['{:4}'.format(n) for n in numerator]))
    print('CORRECT PERCENTILE Y VALUE DENOMINATOR:', denominator)
    yvals = numerator/denominator
    return xvals, yvals


if __name__ == '__main__':
    main()
