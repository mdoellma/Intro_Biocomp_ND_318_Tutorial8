"""
Exercise 8, Python, Question 2
Grant Keller and Kathleen Nicholson
10/23/2017

This script rewrites .vcf files containing RADseq data
to only contain allelic count information. If no data is present
(recognized as a field of ./.:.:.:.:.) then NA is written instead.
Non-data fields are unchanged.

Output is written to outfile, currently CfloridaCounts.txt.
"""
#import packages
from __future__ import print_function
import re


if __name__ == '__main__':

    #assign regex to variable name, or compile to variable name
    TX_RE = re.compile(r'cf\w*?\.a\w*?\.(\d{3})', re.IGNORECASE)
    FL_RE = re.compile(r'cf\w*?\.g\w*?\.(\d{3})', re.IGNORECASE)
    SNP_RE = re.compile(r'^.+?/.+?:(.+?,.+?):.+?:.+?,.+?,.+?$')

    with open('Cflorida.vcf', 'r') as VCFFILE, open('CfloridaCounts.txt', 'w') as OUTFILE:
        for line in VCFFILE:
            line = line.strip()
            line = line.split('\t')
            if line[0][0:2] == '##': # line = header
                # don't do anything
                x = None
            elif line[0] == '#' and line[1] != '#': # line contains column headings
                for i, item in enumerate(line):
                    tx_match, fl_match = TX_RE.match(item), FL_RE.match(item)
                    if tx_match: # if match, stdize to texas name convention
                        line[i] = 'Cf.Sfa.{0}'.format(tx_match.group(1))
                    elif fl_match: # if match, stdize to flordia name convention
                        line[i] = 'Cf.Gai.{0}'.format(fl_match.group(1))
                    else:
                        continue
            else:
                for i, item in enumerate(line):
                    if SNP_RE.match(item):
                        snps = SNP_RE.match(item)
                        line[i] = snps.group(1)
                    elif item == './.:.:.:.:.':
                        line[i] = 'NA'
                    else:
                        continue
            line = '\t'.join(line)
            print(line, file=OUTFILE)
