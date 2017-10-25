#Exercise 8
#Authors: Janice Love and Melissa Stephens

import re

#Open files to read and write
Infile=open("Cflorida.vcf","r")
Outfile=open("CfloridaCounts.txt","w")

#set variables
TxString=[Cc][Ff][0-9]*\.[Aa][0-9]*\.
NewTxString=(Cf)\.(Sfa)\.

FlString=[Cc][Ff]\.[Gg][Aa]*[A-Za-z]*[0-9]*\.)
NewFlString=(Cf)\.(Gai)\.

#for loop
for line in Infile:
        line=line.strip()
        if "##" in line:
                Outfile.write(line + "\n")
        elif "#" in line:
        #need to search through the line for all possible combinations of names (regex string)
	#then replace only the first two sets of information (not the XXX which is unique to each sample)
                re.search([Cc][Ff][0-9]*\.[Aa][0-9]*\., line)
                re.sub([Cc][Ff][0-9]*\.[Aa][0-9]*\.,(Cf)\.(Sfa)\.,line)
                Outfile.write(line + "\n")
