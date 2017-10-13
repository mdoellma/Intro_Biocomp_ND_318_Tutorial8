#Exercise 8, Q1
#Authors: Grant Keller and Kathleen Nicholson

#import packages
import re

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#Assigning regex as a variable
#Names=r""
#SNPs=r""

#Creating a for loop to loop over Cflorida.vcf
for : # ___ in vcffile
    line = line.strip()
    if : #line starts w/##
    #write name to file
    elif : #line starts w/#
    #replace with standard regexes
    re.sub(r"\N")
    #write to file
    else : #this is everything else
    #change full SNPs to allele counts
    re.sub(r"\N")
    #change . to NA using \.
    re.sub(r"\N")
    #write new version to file 