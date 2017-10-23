#Exercise 8, Q1
#Authors: Grant Keller and Kathleen Nicholson

#import packages
from __future__ import print_function
import re

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name
TX_RE = re.compile(r'cf\w*?\.a\w*?\.(\d{3})', re.IGNORECASE)
FL_RE = re.compile(r'cf\w*?\.g\w*?\.(\d{3})', re.IGNORECASE)
SNP_RE = re.compile(r'^.+?/.+?:(.+?,.+?):.+?:.+?,.+?,.+?$')

with open('Cflorida.vcf', 'r') as vcffile, open('CfloridaCounts.txt', 'w') as outfile:
    for line in vcffile:
        line = line.strip()
        line = line.split('\t')
        if line[0][0:2] == '##': # line = header
            # don't do anything
            x = None
        elif line[0] == '#' and line[1] != '#': # line contains column headings
            for i in range(len(line)):
                tx_match, fl_match = TX_RE.match(line[i]), FL_RE.match(line[i])
                if tx_match: # if match, stdize to texas name convention
                    line[i] = 'Cf.Sfa.{0}'.format(tx_match.group(1))
                elif fl_match: # if match, stdize to flordia name convention
                    line[i] = 'Cf.Gai.{0}'.format(fl_match.group(1))
                else:
                    continue
        else:
            for i in range(len(line)):
                if SNP_RE.match(line[i]):
                    snps = SNP_RE.match(line[i])
                    line[i] = snps.group(1)
                elif line[i] == './.:.:.:.:.':
                    line[i] = 'NA'
                else:
                    continue
        line = '\t'.join(line)
        print(line, file=outfile)
