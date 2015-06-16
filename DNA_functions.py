'''
Written by Cham K.
June 16th 2015
Copyright 2015 (MIT License)
'''

def complementary_strand(parent_strand, output_form=0, case='upper'):
    '''(str, int) -> (str)
    Returns sequence of replicated DNA strand.
    Can process upper-case and lower-case parent_strand input with or without whitespace characters.

    Optional parameter return_form modifies format of function output (replicated strand).
    Default value (0) returns each base seperated by whitespace character.
     a)output_form=0 -> output (spaced): A A T G C C
     b)output_form=1 -> output (seperated by codon): AAT GCC
     c)output_form=2 -> output (no spaces): AATGCC

    Optional parameter case determines if output is upper-case or lower-case.
    Default value ('upper') returns output in upper-case.
     a)case='upper' -> output: A A T G C C
     b)case='lower' -> output: a a t g c c
     
    >>>DNA_replication('A A T G C C T A T G G C')
    'T T A C G G A T A C C G'
    >>>DNA_replication('AATGCCTATGGC')
    'T T A C G G A T A C C G'
    >>>DNA_replication('aatgcctatggc', 1)
    'TTA CGG ATA CCG'
    >>>DNA_replication('AATGCCTATGGC', 2, 'lower')
    'ttacggataccg'
    '''
    conversion_dict = {'A':'T','C':'G','T':'A','G':'C'}
    
    replicated_strand = ''
    parent_strand = parent_strand.replace(' ','').upper()
    if output_form == 0:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char] + ' '
            else:
              return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'

        if case == 'upper':
            return replicated_strand.strip()
        if case == 'lower':
            return replicated_strand.lower().strip()
            
    if output_form == 1:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char]
            else:
                return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'

        temp_list = [replicated_strand[i:i+3] for i in range(0, len(replicated_strand), 3)] #storing codons as elements of temp_list
        codon_strand = ' '.join(temp_list)

        if case == 'upper':
            return codon_strand.strip()
        if case == 'lower':
            return codon_strand.lower().strip()

    if output_form == 2:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char]
            else:
                return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'
    
        if case == 'upper':
            return replicated_strand.strip()
        if case == 'lower':
            return replicated_strand.lower().strip()

def base_count(sequence, base):
    ''' (str, str) -> (int)
    Returns the total amount of a specified nitrogenous base (A, T, C, or G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.

    >>>base_count('G A T A C C', 'A')
    2
    >>>base_count('gaataaccgatac', 'A')
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
    
def total_base_count(sequence):
    ''' (str, str) -> (dict)
    Returns a dictionary containing the amount of all bases (A, T, C, and G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.
    
    >>>total_base_count('G A T A C C')
    {'G': 1, 'T': 1, 'A': 2, 'C': 2}
    >>>total_base_count('gaataaccgatac')
    {'T': 2, 'C': 3, 'A': 6, 'G': 2}
    '''
    return {'A':base_count(sequence, 'A'), 'T':base_count(sequence, 'T'), 'C':base_count(sequence, 'C'), 'G':base_count(sequence, 'G')}

def base_composition(sequence, base):
    ''' (str, str) -> (float)
    Returns the amount (percentage rounded to 2 decimal places) of a specified nitrogenous base (A, T, C, or G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.

    >>>base_composition('G A T A C C', 'A')
    33.33
    >>>base_composition('gaataaccgatac', 'T')
    15.38
    '''
    A = base_count(sequence, 'A')
    T = base_count(sequence, 'T')
    C = base_count(sequence, 'C')
    G = base_count(sequence, 'G')
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
    
def total_base_composition(sequence):
    ''' (str, str) -> (dict)
    Returns a dictionary containing percent composition values (rounded to 2 decimal places) of all bases (A, T, C, and G) in a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.
    
    >>>total_base_composition('G A T A C C')
    {'G': 16.67, 'C': 33.33, 'T': 16.67, 'A': 33.33}
    >>>total_base_composition('gaataaccgatac')
    {'A':46.15, 'T':15.38, 'C':15.38, 'G':15.38}
    '''
    return {'A':base_composition(sequence, 'A'), 'T':base_composition(sequence, 'T'), 'C':base_composition(sequence, 'C'), 'G':base_composition(sequence, 'G')}

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
    A = base_count(sequence, 'A')
    T = base_count(sequence, 'T')
    C = base_count(sequence, 'C')
    G = base_count(sequence, 'G')
    if percent == True: return (G+C)/(A+T+C+G)*100
    if percent == False: return (G+C)/(A+T+C+G)

