'''
Written by Cham K.
June 16th 2015
'''

def transcription(parent_strand, output_form=0, case='upper'):
    ''' (str) -> (str)
    Returns an RNA sequence transcribed from a DNA sequence.
    Can process upper-case and lower-case sequence input with or without whitespace characters.

    Optional parameter return_form modifies format of function output (replicated strand).
    Default value (0) returns sequence without whitespace.
     a)output_form=0 -> output (no spaced): AAUGCC
     b)output_form=1 -> output (seperated by codon): AAU GCC
     c)output_form=2 -> output (spaced): A A U G C C

    Optional parameter case determines if output is upper-case or lower-case.
    Default value ('upper') returns output in upper-case.
     a)case='upper' -> output: AAUGCC
     b)case='lower' -> output: aaugcc
    
    >>>transcription('A A T G C C T A T G G C')
    'AAUGCCUAUGGC'
    >>>transcription('AATGCCTATGGC')
    'AAUGCCUAUGGC'
    >>>transcription('aatgcctatggc', 1)
    'AAU GCC UAU GGC'
    >>>transcription('AATGCCTATGGC', 2, 'lower')
    'a a u g c c u a u g g c'
    '''
    
    conversion_dict = {'T':'U','A':'A','C':'C','G':'G'}
    replicated_strand = ''
    parent_strand = parent_strand.replace(' ','').upper()
    
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
