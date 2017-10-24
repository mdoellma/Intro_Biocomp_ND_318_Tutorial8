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
from plotnine import ggplot, aes, xlab, ylab, geom_histogram, ggtitle
from pandas import DataFrame

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
    id_dict = {}
    with open(IDFILE, 'r') as id_file:
        for line in id_file:
            line = line.strip()
            line = line.split('\t')
            if line[0] in id_dict:
                print('Error - read duplicate ID from {}'.format(IDFILE))
                sys.exit(1)
            else:
                id_dict[line[0]] = line[1]
    return id_dict

def find_sequences(id_dict, regex):
    """
    Returns cut site start positions for sequences which can be positively
    identified, as well as those which cannot. Also outputs identifying info
    and sequences to FASTA_OUTFILE and returns info for sequences which could
    not be identified.
    """
    bad_list = []
    good_cutsite_pos = []
    bad_cutsite_pos = []
    with open(SEQFILE, 'r') as fastq, open(FASTA_OUTFILE, 'w') as fasta:
        line = fastq.readline()
        line = line.strip()
        while line != "":
            if line[0] == '@': # checks for header lines
                line = fastq.readline() # if so, skip to next line (seq line)
                line = line.strip()
                if regex.match(line): # is 8bp barcode in seq line?
                    seq = regex.match(line)
                    # p holds positions of match object
                    [None for p in regex.finditer(line)]
                    # first A in AATTC cut site
                    cut_pos = p.start()+len(seq.group(1))+len(seq.group(2))
                    if seq.group(2) in id_dict.keys():
                        good_cutsite_pos.append(cut_pos)
                        print('> {}'.format(id_dict[seq.group(2)]), file=fasta)
                        print(seq.group(3), file=fasta)
                    else:
                        bad_list.append({'BARCODE':seq.group(2),
                                         'SEQUENCE':seq.group(3)})
                        bad_cutsite_pos.append(cut_pos)
                for i in range(3): # skips over +, quality score, next header
                    line = fastq.readline()
                line = line.strip()
            else:
                print('Error: First line not header "@" line. Is format fastq?')
                exit(2)
    return good_cutsite_pos, bad_cutsite_pos, bad_list

def histogram_etc(cuts, headline):
    """
    Given a Pandas DataFrame, and a title (headline), creates a histogram corresponding
    to the start point of cutsites in RADseq data.
    """
    out_hist = ggplot(cuts, aes(x='cutsites'))
    xlabel = xlab('Position Restriction Cutpoint Start')
    ylabel = ylab('Frequency')
    title = ggtitle(headline)
    #Graph histograms of good and bad start positions
    print(out_hist + geom_histogram(binwidth=5) + xlabel + ylabel + title)

if __name__ == '__main__':
    # obtain dictionary of IDs and with 8 bp barcodes as keys
    ID_DICT = get_ids()
    # regex to match sequence lines, capture:
    # 1: pre-barcode sequence    2: 8bp barcode    3: sequence after cutsite
    SEQ_MATCH = re.compile(r'^(\w*?)([ATCG]{8})AATTC(\w+)$')
    # obtains list of cutsites from sequence output to fasta, sequences
    #     whose info were not found in ID_DICT, and info list of bad sequences.
    GOOD_CUTSITES, BAD_CUTSITES, BAD_LIST = find_sequences(ID_DICT, SEQ_MATCH)
    # outputs histogram for "good" cutsites
    histogram_etc(DataFrame(data=GOOD_CUTSITES, columns=['cutsites']), 'Good Cut Sites')
    # outputs histogram for "bad" cutsites
    histogram_etc(DataFrame(data=BAD_CUTSITES, columns=['cutsites']), 'Bad Cut Sites')
