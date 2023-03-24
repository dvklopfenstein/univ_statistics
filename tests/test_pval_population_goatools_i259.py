#!/usr/bin/env python3

from sys import stdout
from goatools.pvalcalc import FisherScipyStats

__copyright__ = "Copyright (C) 2023-present, DV Klopfenstein, PhD. All rights reserved."
__author__ = "DV Klopfenstein, PhD"

# -----------------------------------------------------------------------------------------------
# Maryam-Haghani commented on Jan 27 Hi,
# 
# I performed the enrichment analysis using my background set, and repeated it restricting the
# background set to only include genes with at least one annotation term (based on annotation file
#         that the analysis is using).
# 
# I realized that GOATOOLS takes into account all background set genes without considering whether
# or not each gene has an annotation term. As a result, the findings of these two analyses had
# different P-values and GO term significance levels.
# 
# I'm wondering to know why GOATOOLS does not apply this filter by default in order to do a more
# accurate enrichment study.
# 
# Thanks!
# 
# -----------------------------------------------------------------------------------------------
# Changing the background population genes will most likely result in different pvalues than if
# using the original background population genes. This is correct behavior.
# 
# If the background population genes are reduced by removing unannotated genes, the same should be
# done with the study genes.
# 
# Even with the reduction in both the population and study set of genes, the pvalues will still
# likely to be different than not removing any genes due to the random chance that the distribution
# of unannotated genes in the total population and the distribution of unannotated total study
# population will differ from gene set to gene set. This is expected behavior.
# 
# GOA Tools keeps all study genes and population genes by default. However, reseachers wishing to
# develop criteria to remove population genes are able to do so due to the GOA Tools architecture
# that separates managing the databases (GO ontology DAG and annotations) from running the
# statistical tests.
# 
# Please feel free to apply any filtering functions on the population genes, but also ensure the
# same filter is applied to the study gene sets.


OBJ = FisherScipyStats('fisher_scipy_stats', stdout)

def test_pval_population_i259():
    """Test effect of removing population genes that are not annotated"""
    # Original test
    _get_pval(study_count=4, study_all=20, pop_count=40, pop_all=1000)
    # Population is stripped of genes not annotated
    _get_pval(study_count=4, study_all=20, pop_count=40, pop_all=750)
    # Population and study sets stripped of genes not annotated
    _get_pval(study_count=3, study_all=15, pop_count=30, pop_all=750)

def _get_pval(study_count, study_all, pop_count, pop_all):
    pval = OBJ.calc_pvalue(study_count, study_all, pop_count, pop_all)
    print(f'{pop_all:4}=Total population {pval:10.4g}=pval')


if __name__ == '__main__':
    test_pval_population_i259()

# Copyright (C) 2023-present DV Klopfenstein, PhD. All rights reserved.
