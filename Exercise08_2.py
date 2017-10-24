"""
Exercise 8, Python, Question 2
Grant Keller and Kathleen Nicholson
10/23/2017

SHELL USAGE: python Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA
IPYTHON USAGE: run Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA
"""

from __future__ import print_function
import re
import sys

try:
    IDFILE = sys.argv[1]
except IndexError:
    print('USAGE: python Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA')
    IDFILE = raw_input('ID File: ')
try:
    SEQFILE = sys.argv[2]
except IndexError:
    print('USAGE: python Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA')
    SEQFILE = raw_input('SEQ File: ')
try:
    FASTA_OUTFILE = sys.argv[3]
except IndexError:
    print('USAGE: python Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA')
    FASTA_OUTFILE = raw_input('Fasta File (Output): ')

def get_ids():
    """
    Returns a dictionary from a tab delimited ID file, using the
    DNA barcodes as dict keys, and the sequence IDs as values.
    """
    ID_DICT = {}
    with open(IDFILE, 'r') as id_file:
        for line in id_file:
            line = line.strip()
            line = line.split('\t')
            if line[0] in ID_DICT:
                print('Error - read duplicate ID from {}'.format(IDFILE))
                sys.exit(1)
            else:
                ID_DICT[line[0]] = line[1]
    return ID_DICT

def find_sequences(ID_DICT, MATCH):
    bad_list = []
    cutsite_pos_list = []
    with open(SEQFILE, 'r') as fastq, open(FASTA_OUTFILE, 'w') as fasta:
        line = fastq.readline()
        line = line.strip()
        while line != "":
            if line[0] == '@': # checks for header lines
                line = fastq.readline() # if so, skip to next line (seq line)
                line = line.strip()
                if MATCH.match(line): # is 8bp barcode in seq line?
                    seq = MATCH.match(line)
                    if seq.group(2) in ID_DICT.keys():
                        [None for p in MATCH.finditer(line)] # p holds positions of match object
                        cut_pos = p.start()+len(seq.group(1))+len(seq.group(2)) # first A in AATTC cut site
                        cutsite_pos_list.append(cut_pos)
                        print('> {}'.format(ID_DICT[seq.group(2)]), file=fasta)
                        print(seq.group(3), file=fasta)
                    else:
                        bad_list.append({'BARCODE':seq.group(2),
                                         'SEQUENCE':seq.group(3)})
                for i in range(3): # skips over +, quality score, next header
                    line = fastq.readline()
                line = line.strip()                    
            else:
                print('Error: First line not header "@" line. Is format fastq?')
                exit(2)
    return cutsite_pos_list, bad_list

def histogram_etc():
    #Graph histograms of good and bad start positions
    pass

if __name__ == '__main__':
    ID_DICT = get_ids()
    SEQ_MATCH = re.compile(r'(\w*?)([ATCG]{8})AATTC(\w+)$')
    cutsite_pos_list, bad_list = find_sequences(ID_DICT, SEQ_MATCH)
