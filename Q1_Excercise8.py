#Exercise 8
#Authors: Janice Love and Melissa Stephens

import re

#Open files to read and write
Infile=open("Cflorida.vcf","r")
Outfile=open("CfloridaCounts.txt","w")

#for loop
for line in Infile:
	line.strip()
	if ## in line:
		Outfile.write(line + "\n")
	elif # in line:
		
		
