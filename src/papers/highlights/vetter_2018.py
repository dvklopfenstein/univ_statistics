# -*- coding: utf-8 -*-
"""Highlights from a research paper done with Kindle"""

__copyright__ = 'Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved'
from collections import namedtuple


# NEW(63) USR(0) highlights
NTD = namedtuple('NTD', 'color page name text tags')
# pylint: disable=line-too-long
NTS = [

    # TEXT: Inferential statistics essentially allows investigators to make a vali
    # NTD._make(['yellow', 1, '', 'Inferential statistics essentially allows investigators to make a valid inference about an association of interest for a specific population that is based on data collected from a random sample of that population.', ['Vetter_2018']]),

    # TEXT: UNPAIRED t TEST
    # NTD._make(['yellow', 1, '', 'UNPAIRED t TEST', ['Vetter_2018']]),

    # TEXT: The unpaired or independent samples t test is used to test and possibl
    # NTD._make(['yellow', 1, '', 'The unpaired or independent samples t test is used to test and possibly to reject the null hypothesis that the 2 population means are equal (Ho: µ1 = µ2),', ['Vetter_2018']]),

    # TEXT: Unadjusted Bivariate Two-Group Comparisons: When Simpler is Better
    # NTD._make(['yellow', 1, '', 'Unadjusted Bivariate Two-Group Comparisons: When Simpler is Better', ['Vetter_2018']]),

    # TEXT: 1. Independent variable is categorical (ie, 2 study groups).
    # NTD._make(['yellow', 2, '', '1. Independent variable is categorical (ie, 2 study groups).', ['Vetter_2018']]),

    # TEXT: 2. Dependent variable is continuous (ie, interval or ratio data).
    # NTD._make(['yellow', 2, '', '2. Dependent variable is continuous (ie, interval or ratio data).', ['Vetter_2018']]),

    # TEXT: 3. Values are independent within each of the 2 samples.
    # NTD._make(['yellow', 2, '', '3. Values are independent within each of the 2 samples.', ['Vetter_2018']]),

    # TEXT: 4. Two samples are independent of each other.
    # NTD._make(['yellow', 2, '', '4. Two samples are independent of each other.', ['Vetter_2018']]),

    # TEXT: 5. There is approximately normal distribution of the dependent variabl
    # NTD._make(['yellow', 2, '', '5. There is approximately normal distribution of the dependent variable data for each group.', ['Vetter_2018']]),

    # TEXT: 6. There are approximately equal (homogeneous) variances of the data a
    # NTD._make(['yellow', 2, '', '6. There are approximately equal (homogeneous) variances of the data across the 2 groups.', ['Vetter_2018']]),

    # TEXT: PAIRED t TEST
    # NTD._make(['yellow', 2, '', 'PAIRED t TEST', ['Vetter_2018']]),

    # TEXT: 1. The paired values are randomly sampled from or are at least represe
    # NTD._make(['yellow', 2, '', '1. The paired values are randomly sampled from or are at least representative of the underlying population of paired samples.', ['Vetter_2018']]),

    # TEXT: 2. Each pair of values is selected independently of the other pairs.
    # NTD._make(['yellow', 2, '', '2. Each pair of values is selected independently of the other pairs.', ['Vetter_2018']]),

    # TEXT: 3. The differences between the paired or matched values are normally d
    # NTD._make(['yellow', 2, '', '3. The differences between the paired or matched values are normally distributed (Gaussian distribution).', ['Vetter_2018']]),

    # TEXT: CHI-SQUARE TEST FOR ASSOCIATION
    # NTD._make(['yellow', 2, '', 'CHI-SQUARE TEST FOR ASSOCIATION', ['Vetter_2018']]),

    # TEXT: Chi-square for R × C Tables
    # NTD._make(['yellow', 2, '', 'Chi-square for R × C Tables', ['Vetter_2018']]),

    # TEXT: The Pearson chi-square test is widely used to test the null hypothesis
    # NTD._make(['yellow', 2, '', 'The Pearson chi-square test is widely used to test the null hypothesis that 2 unpaired categorical variables, each with 2 or more nominal levels (values), are independent of each other (Table).', ['Vetter_2018']]),

    # TEXT: 1. Two independent categorical variables, each measured on a set of su
    # NTD._make(['yellow', 3, '', '1. Two independent categorical variables, each measured on a set of subjects.', ['Vetter_2018']]),

    # TEXT: 2. Each variable can have 2 or more categories.
    # NTD._make(['yellow', 3, '', '2. Each variable can have 2 or more categories.', ['Vetter_2018']]),

    # TEXT: 3. Each variable should be nominal, such that there is no natural orde
    # NTD._make(['yellow', 3, '', '3. Each variable should be nominal, such that there is no natural ordering of its levels or values.', ['Vetter_2018']]),

    # TEXT: 4. There is a sufficient number of observations in each cell of the R
    # NTD._make(['yellow', 3, '', '4. There is a sufficient number of observations in each cell of the R × C table.', ['Vetter_2018']]),

    # TEXT: Ordinal Categories
    # NTD._make(['yellow', 3, '', 'Ordinal Categories', ['Vetter_2018']]),

    # TEXT: z Test for 2-Group Proportions
    # NTD._make(['yellow', 3, '', 'z Test for 2-Group Proportions', ['Vetter_2018']]),

    # TEXT: CHI-SQUARE SINGLE SAMPLE GOODNESS OF FIT TEST
    # NTD._make(['yellow', 3, '', 'CHI-SQUARE SINGLE SAMPLE GOODNESS OF FIT TEST', ['Vetter_2018']]),

    # TEXT: WILCOXON-MANN-WHITNEY TEST (MANNWHITNEY U TEST, WILCOXON RANK SUM TEST
    # NTD._make(['yellow', 4, '', 'WILCOXON-MANN-WHITNEY TEST (MANNWHITNEY U TEST, WILCOXON RANK SUM TEST)', ['Vetter_2018']]),

    # TEXT: When comparing 2 groups on an ordinal or nonnormally distributed conti
    # NTD._make(['orange', 4, '', 'When comparing 2 groups on an ordinal or nonnormally distributed continuous outcome variable, the 2-sample t test is usually not appropriate.', ['Vetter_2018']]),

    # TEXT: This test is akin to a t test on the ranks of the data.33
    # NTD._make(['yellow', 4, '', 'This test is akin to a t test on the ranks of the data.33', ['Vetter_2018']]),

    # TEXT: Data are ranked from smallest to largest while ignoring group assignme
    # NTD._make(['orange', 4, '', 'Data are ranked from smallest to largest while ignoring group assignment, then the groups are compared on the mean rank (accounting for ties).34', ['Vetter_2018']]),

    # TEXT: the null hypothesis for the Mann-Whitney test is Ho: P(X &gt; Y) = .5.
    # NTD._make(['orange', 4, '', 'the null hypothesis for the Mann-Whitney test is Ho: P(X &gt; Y) = .5.', ['Vetter_2018']]),

    # TEXT: In other words, the probability that a randomly sampled patient from g
    # NTD._make(['yellow', 4, '', 'In other words, the probability that a randomly sampled patient from group 1 has a higher value than a randomly sampled patient from group 2 is equal to .50, or a coin flip.', ['Vetter_2018']]),

    # TEXT: 1. Random samples are for 2 populations.
    # NTD._make(['yellow', 4, '', '1. Random samples are for 2 populations.', ['Vetter_2018']]),

    # TEXT: 2. Outcomes are independent within samples.
    # NTD._make(['yellow', 4, '', '2. Outcomes are independent within samples.', ['Vetter_2018']]),

    # TEXT: 3. Measurement scale is at least ordinal.
    # NTD._make(['yellow', 4, '', '3. Measurement scale is at least ordinal.', ['Vetter_2018']]),

    # TEXT: 4. Variance of outcome is the same for each group.
    # NTD._make(['yellow', 4, '', '4. Variance of outcome is the same for each group.', ['Vetter_2018']]),

    # TEXT: The Wilcoxon-Mann-Whitney test assesses whether there is a location or
    # NTD._make(['yellow', 4, '', 'The Wilcoxon-Mann-Whitney test assesses whether there is a location or pattern shift between the 2 populations of interest.35', ['Vetter_2018']]),

    # TEXT: If the null is rejected, one concludes that values of one group tend t
    # NTD._make(['orange', 4, '', 'If the null is rejected, one concludes that values of one group tend to be higher than the other group.', ['Vetter_2018']]),

    # TEXT: Exemplary uses of this test might be to compare randomized or propensi
    # NTD._make(['yellow', 4, '', 'Exemplary uses of this test might be to compare randomized or propensity-matched groups on an ordinal outcome such a numerical rating scale pain score, or a skewed (nonnormally distributed) variable like opioid consumption.', ['Vetter_2018']]),

    # TEXT: An extension of the Wilcoxon-Mann-Whitney test for comparing more than
    # NTD._make(['orange', 4, '', 'An extension of the Wilcoxon-Mann-Whitney test for comparing more than 2 groups is the Kruskal-Wallis test.20,33,34', ['Vetter_2018']]),

    # TEXT: When reporting Wilcoxon-Mann-Whitney test results, it is important to
    # NTD._make(['yellow', 4, '', 'When reporting Wilcoxon-Mann-Whitney test results, it is important to avoid stating that a significant result implies that there is evidence that the medians differ or that they do not differ.', ['Vetter_2018']]),

    # TEXT: The test does not explicitly compare medians, but rather a general loc
    # NTD._make(['orange', 4, '', 'The test does not explicitly compare medians, but rather a general location or pattern shift.35', ['Vetter_2018']]),

    # TEXT: In fact, it is quite possible to have a valid statistically significan
    # NTD._make(['yellow', 4, '', 'In fact, it is quite possible to have a valid statistically significant Wilcoxon-Mann-Whitney result when the observed medians are exactly the same.', ['Vetter_2018']]),

    # TEXT: Results for the Wilcoxon-Mann-Whitney can be sufficiently reported as
    # NTD._make(['orange', 4, '', 'Results for the Wilcoxon-Mann-Whitney can be sufficiently reported as the median (interquartile range) for each group, along with the median difference between groups and its confidence interval, calculated using the Hodges-Lehman estimator.36', ['Vetter_2018']]),

    # TEXT: It is also appropriate to report the observed MannWhitney probability,
    # NTD._make(['yellow', 4, '', 'It is also appropriate to report the observed MannWhitney probability, P(X &gt; Y), simply called “p.”', ['Vetter_2018']]),

    # TEXT: It can be even more informative to report the odds for this probabilit
    # NTD._make(['orange', 4, '', 'It can be even more informative to report the odds for this probability, or p/(1 − p), which is called the Wilcoxon-Mann-Whitney odds.', ['Vetter_2018']]),

    # TEXT: A confidence interval for the Wilcoxon-Mann-Whitney odds should also b
    # NTD._make(['yellow', 4, '', 'A confidence interval for the Wilcoxon-Mann-Whitney odds should also be reported.', ['Vetter_2018']]),

    # TEXT: Further details, including sample size calculations and full examples,
    # NTD._make(['orange', 4, '', 'Further details, including sample size calculations and full examples, are provided in the excellent article by Divine et al.37', ['Vetter_2018']]),

    # TEXT: The authors reported that compared to placebo, the median intraoperati
    # NTD._make(['yellow', 4, '', 'The authors reported that compared to placebo, the median intraoperative opioid use was reduced in the dexmedetomidine group but not at 24 hours postoperatively.', ['Vetter_2018']]),

    # TEXT: As compared to placebo, no difference in median pain scores, as measur
    # NTD._make(['orange', 4, '', 'As compared to placebo, no difference in median pain scores, as measured by an 11-point discrete scale, was observed at 24 and at 48 hours postoperatively in the dexmedetomidine group.38', ['Vetter_2018']]),

    # TEXT: As mentioned above, while this was an appropriate use of the Wilcoxon-
    # NTD._make(['yellow', 4, '', 'As mentioned above, while this was an appropriate use of the Wilcoxon-Mann-Whitney test, the correct interpretation would be that values of intraoperative opioid use were reduced (not that the median per se was reduced) in 1 group versus the other.', ['Vetter_2018']]),

    # TEXT: Naik et al38 could also have reported the median difference and its co
    # NTD._make(['orange', 4, '', 'Naik et al38 could also have reported the median difference and its confidence interval, as well as the Wilcoxon-Mann-Whitney probability and odds.', ['Vetter_2018']]),

    # TEXT: WILCOXON SIGNED-RANK TEST
    # NTD._make(['yellow', 4, '', 'WILCOXON SIGNED-RANK TEST', ['Vetter_2018']]),

    # TEXT: When making paired comparisons on data that are ordinal, or continuous
    # NTD._make(['yellow', 4, '', 'When making paired comparisons on data that are ordinal, or continuous but nonnormally distributed, the Wilcoxon signed-rank test can be used.20,33,34,39', ['Vetter_2018']]),

    # TEXT: It is an alternative to the paired t test when the paired differences
    # NTD._make(['orange', 4, '', 'It is an alternative to the paired t test when the paired differences do not appear to be normally distributed.34', ['Vetter_2018']]),

    # TEXT: Typical uses of this test would be comparing patients from before to a
    # NTD._make(['yellow', 4, '', 'Typical uses of this test would be comparing patients from before to after an intervention or procedure, such as surgery.', ['Vetter_2018']]),

    # TEXT: Results could best be reported as the median difference and confidence
    # NTD._make(['orange', 4, '', 'Results could best be reported as the median difference and confidence interval for the difference.', ['Vetter_2018']]),

    # TEXT: Technically, it is used to assess whether 2 dependent samples were sel
    # NTD._make(['yellow', 4, '', 'Technically, it is used to assess whether 2 dependent samples were selected from the populations having the same distribution.', ['Vetter_2018']]),

    # TEXT: 1. Data are paired and come from the same population.
    # NTD._make(['yellow', 4, '', '1. Data are paired and come from the same population.', ['Vetter_2018']]),

    # TEXT: 2. Each pair is chosen randomly and independently.
    # NTD._make(['yellow', 4, '', '2. Each pair is chosen randomly and independently.', ['Vetter_2018']]),

    # TEXT: 3. The data are at least ordinal.
    # NTD._make(['yellow', 4, '', '3. The data are at least ordinal.', ['Vetter_2018']]),

    # TEXT: In their study of the influence of nociceptive stimulation on the anal
    # NTD._make(['yellow', 4, '', 'In their study of the influence of nociceptive stimulation on the analgesia nociception index (ANI) during propofol–remifentanil anesthesia, Gruenewald et al40 applied a Wilcoxon signed-rank test.', ['Vetter_2018']]),

    # TEXT: Specifically, the primary outcome variables of the ANI and the surgica
    # NTD._make(['orange', 4, '', 'Specifically, the primary outcome variables of the ANI and the surgical pleth index were obtained in 25 patients before and after nociceptive stimulation.', ['Vetter_2018']]),

    # TEXT: Each study subject thus provided paired data for the Wilcoxon signed-r
    # NTD._make(['yellow', 4, '', 'Each study subject thus provided paired data for the Wilcoxon signed-rank test.', ['Vetter_2018']]),

    # TEXT: The ANI and surgical pleth index were significantly changed by the ins
    # NTD._make(['orange', 4, '', 'The ANI and surgical pleth index were significantly changed by the insertion of a laryngeal mask airway and the delivery of neuromuscular tetanic stimulation.40', ['Vetter_2018']]),
]

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
