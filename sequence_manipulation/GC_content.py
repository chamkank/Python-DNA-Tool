'''
Written by Cham K.
June 16th 2015
'''

from sequence_manipulation import nucleotide_count

def GC_content(sequence, percent=True):
    ''' (str, bool) -> (float)
    Returns the GC-content as a non-rounded percentage (or ratio if percent=False) of a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.
    >>> GC_content('G A T A C C')
    50.0
    >>> GC_content('G A A A T C A C C')
    44.44444444444444
    >>> GC_content('G A A A T C A C C', False)
    0.4444444444444444
    '''
    module = nucleotide_count
    A = module.nucleotide_count(sequence, 'A')
    T = module.nucleotide_count(sequence, 'T')
    C = module.nucleotide_count(sequence, 'C')
    G = module.nucleotide_count(sequence, 'G')
    if percent == True: return (G+C)/(A+T+C+G)*100
    elif percent == False: return (G+C)/(A+T+C+G)
