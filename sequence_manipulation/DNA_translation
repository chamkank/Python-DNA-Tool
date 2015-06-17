'''
Written by Cham K.
June 16th 2015
'''

def translation(parent_strand, output_form=0, case='upper', reverse=False):
    '''(str) -> (str)
    Returns sequence of replicated DNA strand.
    Can process upper-case and lower-case parent_strand input with or without whitespace characters.

    Optional parameter return_form modifies format of function output (replicated strand).
    Default value (0) returns sequence without whitespace.
     a)output_form=0 -> output (no spaced): AATGCC
     b)output_form=1 -> output (seperated by codon): AAT GCC
     c)output_form=2 -> output (spaced): A A T G C C

    Optional parameter case determines if output is upper-case or lower-case.
    Default value ('upper') returns output in upper-case.
     a)case='upper' -> output: AATGCC
     b)case='lower' -> output: aatgcc

    Optional parameter reverse determines if parent_strand is reversed before translation, returning the reverse complement of the DNA sequence.
    Default value (False) does not reverse the sequence before translation.
     a)reverse=False -> output: AATGCC
     b)reverse=True -> output: CCGTAA

    >>>translation('A A T G C C T A T G G C')
    'TTACGGATACCG'
    >>>translation('AATGCCTATGGC', reverse=True)
    'TTACGGATACCG'
    >>>translation('aatgcctatggc', 1)
    'TTA CGG ATA CCG'
    >>>translation('AATGCCTATGGC', 2, 'lower')
    't t a c g g a t a c c g'
    >>>translation('AATGCCTATGGC', 2, 'lower', True)
    'g c c a t a g g c a t t'
    >>>translation('AATGCCTATGGC', reverse=True)
    'GCCATAGGCATT'
    '''

    conversion_dict = {'A':'T','C':'G','T':'A','G':'C'} 
    replicated_strand = ''
    parent_strand = parent_strand.replace(' ','').upper()
    if reverse == True:
        parent_strand = parent_strand[::-1]
    if output_form == 0:
        for char in parent_strand:
            if char in conversion_dict.keys():
                replicated_strand += conversion_dict[char]
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
                replicated_strand += conversion_dict[char] + ' '
            else:
              return 'ERROR: Invalid parent_strand input (raw ATCG-base DNA sequence required).'

        if case == 'upper':
            return replicated_strand.strip()
        if case == 'lower':
            return replicated_strand.lower().strip()

