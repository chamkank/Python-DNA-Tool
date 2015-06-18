def mendel_first(homozygous_dominant, heterozygous, homozygous_recessive):
    ''' (int, int, int) -> float
    Input amount of members of each group in a population.
    Returns the probability (to 6 decimal places) that 2 randomly selected organisms will produce an individual with a dominant allele/phenotype.

    >>> mendel_first(5,10,5)
    0.756579

    >>> mendel_first(100,10,6)
    0.991567
    '''
    a = homozygous_dominant
    b = heterozygous
    c = homozygous_recessive
    probability = 0.0
    probability = ((a**2 - a) + 2*(a*b) + (.75*(b**2 - b)) + 2*(a*c) + 2*(.5*b*c))/((a + b + c)*(a + b + c -1))
    return float("%.6f" % probability)
