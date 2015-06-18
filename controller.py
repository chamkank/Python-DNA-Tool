'''
Written by Cham K.
June 16th 2015

IMPORTANT:
Import this file to access all packages in this project with only function names.
Doing so will eliminate the need to import separate scripts and call functions with full file names (see variables below).
'''

from sequence_manipulation import GC_content
from sequence_manipulation import nucleotide_composition
from sequence_manipulation import nucleotide_count
from sequence_manipulation import RNA_transcription
from sequence_manipulation import DNA_translation
from population_tools import laws_of_mendel

#sequence_manipulation\GC_content.py
GC_content = GC_content.GC_content

#sequence_manipulation\nucleotide_composition.py
total_nucleotide_composition = nucleotide_composition.total_nucleotide_composition
nucleotide_composition = nucleotide_composition.nucleotide_composition

#sequence_manipulation\nucleotide_count.py
total_nucleotide_count = nucleotide_count.total_nucleotide_count
nucleotide_count = nucleotide_count.nucleotide_count

#sequence_manipulation\RNA_transcription.py
transcription = RNA_transcription.transcription

#sequence_manipulation\DNA_translation.py
translation = DNA_translation.translation

#population_tools\laws_of_mendel.py
mendel_first = laws_of_mendel.mendel_first
