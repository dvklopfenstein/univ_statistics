#!/usr/bin/env python3
"""Practice: ocw.jhsph.edu/courses/StatisticalReasoning1/PDFs/2009/PP/SR1_lec1c_pp.pdf"""

import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import seaborn as sns

def test_mead():
    """Income of 9 randomly chosen students Hoplins MPH program"""
    fout_png = 'doc/images/mcgready_lec1c_income.png'
    data = { #      min                        median                        max
        'income1': [12000, 17000, 33000, 34000, 37000, 56000, 72000, 102000, 111000],
        'income2': [17000, 17000, 31000, 33000, 37000, 56000, 72000, 102000, 111000]}

    dfrm = pd.DataFrame(data, columns=['income1', 'income2'])
    _plt(fout_png, dfrm)

def _plt(fout_png, dfrm):
    """Plot data"""
    sns.catplot(data=dfrm)
    sns.boxplot(data=dfrm, showmeans=True, boxprops={'alpha':.3})
    for ylabel in dfrm.columns:
        _vals(ylabel, dfrm)
    plt.savefig(fout_png)
    print('  WROTE: {PNG}'.format(PNG=fout_png))

def _vals(ylabel, dfrm):
    """Get summary statistic values"""
    # Get column index
    xval = dfrm.columns.get_loc(ylabel)
    # Get summary statistics
    mean_val = dfrm[ylabel].mean()
    median_val = dfrm[ylabel].median()
    min_val = dfrm[ylabel].min()
    max_val = dfrm[ylabel].max()
    mean_str = 'Avg {N:,}'.format(N=int(round(mean_val)))
    median_str = 'Median {N:,}'.format(N=int(round(median_val)))
    min_str = 'Min {N:,}'.format(N=int(round(min_val)))
    max_str = 'Max {N:,}'.format(N=int(round(max_val)))
    # Add arrows
    axes = plt.gca()
    kws = {
        'arrowprops': dict(arrowstyle='-|>', fc="k", ec="k", lw=1.5),
        # space between arrow end and text
        'bbox': dict(pad=5, facecolor="none", edgecolor="none")}
    axes.annotate(mean_str, xy=(xval, mean_val), xytext=(xval+.12, mean_val), **kws)
    axes.annotate(median_str, xy=(xval, median_val), xytext=(xval+.05, 2.0*median_val/3.0), **kws)
    axes.annotate(min_str, xy=(xval, min_val), xytext=(xval+.1, min_val/2.0), **kws)
    axes.annotate(max_str, xy=(xval, max_val), xytext=(xval+.1, 3.0*max_val/4.0), **kws)

if __name__ == '__main__':
    test_mead()
