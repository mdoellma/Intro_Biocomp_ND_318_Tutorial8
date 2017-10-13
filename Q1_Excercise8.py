#Exercise 8
#Authors: Janice Love and Melissa Stephens

import re

#Open files to read and write
Infile=open("Cflorida.vcf","r")
Outfile=open("CfloridaCounts.txt","w")

#for loop
for line in Infile:
	line=line.strip()
	if "##" in line:
		Outfile.write(line + "\n")
	elif "#" in line:
	#need to search through the line for all possible combinations of names (regex string)
	#need to backreference and sub each position in the string
		re.search([A-Za-z]{2}[0-9]*\.[A-Za-z][0-9]*\., line)
		re.sub([A-Za-z]{2}[0-9]*\.[A-Za-z][0-9]*\.,(Cf)\.(Sfa)\.,line)
		Outfile.write(line + "\n")
	else:
