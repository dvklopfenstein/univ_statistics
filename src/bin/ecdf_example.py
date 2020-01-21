#!/usr/bin/env python3
"""Example plotting of ECDF"""
# https://stackoverflow.com/questions/15792552/numpy-scipy-equivalent-of-r-ecdfxx-function/37660583#37660583

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

def main():
    fout_png = 'ex_grades_ecdf.png'
    grades = (93.5,93,60.8,94.5,82,87.5,91.5,99.5,86,93.5,92.5,78,76,69,94.5,
              89.5,92.8,78,65.5,98,98.5,92.3,95.5,76,91,95,61)
    
    xs, ys = ecdf_wrong(grades)
    plt.plot(xs, ys, label="wrong cumsum")
    xs, ys = ecdf(grades)
    plt.plot(xs, ys, label="handwritten", marker=">", markerfacecolor='none')
    cdf = ECDF(grades)
    plt.plot(cdf.x, cdf.y, label="statmodels", marker="<", markerfacecolor='none')
    plt.title('Good v Bad ECDF')
    plt.xlabel('Grades')
    plt.legend(loc=2)
    plt.savefig(fout_png)
    print('  WROTE: {PNG}'.format(PNG=fout_png))

def ecdf_wrong(x):
    xs = np.sort(x) # need to be sorted
    ys = np.cumsum(xs)/np.sum(xs) # normalize so sum == 1
    return (xs,ys)

def ecdf(x):
    xs = np.sort(x)
    num_xs = len(xs)
    # Y values are evenly spaced values within a givein interval
    ys = np.arange(1, num_xs+1)/float(num_xs)
    return xs, ys


if __name__ == '__main__':
    main()
