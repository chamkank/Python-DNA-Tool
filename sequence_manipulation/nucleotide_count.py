'''
Written by Cham K.
June 16th 2015
'''

def nucleotide_count(sequence, base):
    ''' (str, str) -> (int)
    Returns the total amount of a specified nitrogenous base (A, T, C, or G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.

    >>>nucleotide_count('G A T A C C', 'A')
    2
    >>>nucleotide_count('gaataaccgatac', 'A')
    6
    '''
    counter = 0
    sequence = sequence.replace(' ','').upper()
    if base == 'A':
        for char in sequence:
            if char == 'A': counter += 1
    elif base == 'T':
        for char in sequence:
            if char == 'T': counter += 1
    elif base == 'C':
        for char in sequence:
            if char == 'C': counter += 1
    elif base == 'G':
        for char in sequence:
            if char == 'G': counter += 1
    else:
        return "ERROR: Null or invalid input recieved for base argument. Base value can be 'A', 'T', 'C', or 'G'."
    return counter
    
def total_nucleotide_count(sequence):
    ''' (str, str) -> (dict)
    Returns a dictionary containing the amount of all bases (A, T, C, and G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.
    
    >>>total_nucleotide_count('G A T A C C')
    {'G': 1, 'T': 1, 'A': 2, 'C': 2}
    >>>total_nucleotide_count('gaataaccgatac')
    {'T': 2, 'C': 3, 'A': 6, 'G': 2}
    '''
    return {'A':nucleotide_count(sequence, 'A'), 'T':nucleotide_count(sequence, 'T'), 'C':nucleotide_count(sequence, 'C'), 'G':nucleotide_count(sequence, 'G')}
