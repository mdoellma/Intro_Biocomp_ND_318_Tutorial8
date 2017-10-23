"""
Exercise 8, Python, Question 2
Grant Keller and Kathleen Nicholson
10/23/2017

SHELL USAGE: python Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA
IPYTHON USAGE: run Exercise08_2.py IDFILE FASTQFILE OUTFILE.FASTA
"""

from __future__ import print_function
from sys import exit, argv

IDFILE = argv[1]
SEQFILE = argv[2]
FASTA_OUTFILE = argv[3]

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
                exit(1)
            else:
                ID_DICT[line[0]] = line[1]
    return ID_DICT
def find_sequences(ID_DICT, MATCH):
    #A while loop will allow us to skip operating on fastq lines we don't care about
    #it also allows us to read huge files line by line, without storing them in memory
    #read and strip the first line in the file
    pass
    with open(SEQFILE, 'r') as fastq:
        line = fastq.readline()
        line = line.strip()
        while line != "":
            if line[0] == '@': # checks for header lines
                line = fastq.readline() # if so, skip to next line (seq line)
                line = line.strip()
                
                if : #is your regex in the sequence
                    #store your regex matches
                    if : #is your DNA barcode in the ID data frame?
                        ##append the start position of the AATTC to your vector
                        #write the fasta header to your file by getting the correct ID from the data frame
                        #write the sequence remaining to the right of the AATTC cut site to your file
                    else:
                        #Optional: append location of AATTC to "bad" vector (pattern found but no barcode match) as above
                for i in range(3): # skips over +, quality score, next header
                    line = file.readline()
                line = line.strip()                    
            else:
                #it's a good idea to break loop and print error message if you end up here
                #this means you've read the wrong number of lines or the input file isn't in the right format (it is!)

def histogram_etc():
    #Graph histograms of good and bad start positions
    pass

if __name__ == '__main__':
    try:
        ID_DICT = get_ids()
        SEQ_CRIT = re.match(r'(()()())')
        #assign regex to variable name, or compile to variable name
        # SOME_VAR = find_sequences(ID_DICT, MATCH)
    except IndexError:
        print('If you\'re using a Python shell try "run Exercise08_2.py indivIDs.txt seqFastq.fq IDseq.fasta".')
    