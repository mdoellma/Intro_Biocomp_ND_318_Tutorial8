#Exercise 8, Q1
#Authors: Grant Keller and Kathleen Nicholson

#import packages
import re

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name
TX_RE = re.compile(r'cf\w*?\.a\w*?\.(\d{3})', re.IGNORECASE)
FL_RE = re.compile(r'cf\w*?\.g\w*?\.(\d{3})', re.IGNORECASE)

with open('Cflorida.vcf', 'r') as vcffile, open('CfloridaCounts.txt', 'w') as outfile:
    for line in vcffile:
        line = line.strip()
        if line[0:2] == '##': # line = header
            print(line, file=outfile)
            continue
        elif line[0] == '#' and line[1] != '#': # line contains column headings
            line = line.split('\t')
            for i in range(len(line)):
                tx_match, fl_match = TX_RE.match(line[i]), FL_RE.match(line[i])
                if tx_match: # if match, stdize to texas name convention
                    line[i] = 'Cf.Sfa.{0}'.format(tx_match.group(1))
                elif fl_match: # if match, stdize to flordia name convention
                    line[i] = 'Cf.Gai.{0}'.format(fl_match.group(1))
                else:
                    continue
            '\t'.join(line)
            print(line, file=outfile)
        else: #now you're in the data
            #replace full SNP info with allele counts only
            #replace missing data with NA
            #write new version of line to new file
