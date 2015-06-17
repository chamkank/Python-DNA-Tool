'''
Written by Cham K.
June 16th 2015
'''

from sequence_manipulation import nucleotide_count

def nucleotide_composition(sequence, base):
    ''' (str, str) -> (float)
    Returns the amount (percentage rounded to 2 decimal places) of a specified nitrogenous base (A, T, C, or G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.

    >>>nucleotide_composition('G A T A C C', 'A')
    33.33
    >>>nucleotide_composition('gaataaccgatac', 'T')
    15.38
    '''
    module = nucleotide_count
    A = module.nucleotide_count(sequence, 'A')
    T = module.nucleotide_count(sequence, 'T')
    C = module.nucleotide_count(sequence, 'C')
    G = module.nucleotide_count(sequence, 'G')
    total_bases = A + T + C + G

    if base == 'A':
        return float("%.2f" % ((A/total_bases)*100))
    if base == 'T':
        return float("%.2f" % ((T/total_bases)*100))
    if base == 'C':
        return float("%.2f" % ((C/total_bases)*100))
    if base == 'G':
        return float("%.2f" % ((G/total_bases)*100))
    else:
        return "ERROR: Null or invalid input recieved for base argument. Base value can be 'A', 'T', 'C', or 'G'."
    
def total_nucleotide_composition(sequence):
    ''' (str, str) -> (dict)
    Returns a dictionary containing percent composition values (rounded to 2 decimal places) of all bases (A, T, C, and G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.
    
    >>>total_nucleotide_composition('G A T A C C')
    {'G': 16.67, 'C': 33.33, 'T': 16.67, 'A': 33.33}
    >>>total_nucleotide_composition('gaataaccgatac')
    {'A':46.15, 'T':15.38, 'C':15.38, 'G':15.38}
    '''
    return {'A':nucleotide_composition(sequence, 'A'), 'T':nucleotide_composition(sequence, 'T'), 'C':nucleotide_composition(sequence, 'C'), 'G':nucleotide_composition(sequence, 'G')}
