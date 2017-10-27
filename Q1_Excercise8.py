#Exercise 8
#Authors: Janice Love and Melissa Stephens

import re

#Open files to read and write
Infile=open("Cflorida.vcf","r")
Outfile=open("CfloridaCounts.txt","w")

#set variables
TxString=r"[Cc][Ff][0-9]*\.[Aa][0-9]*\."
FlString=r"[Cc][Ff]\.[Gg][Aa]*[A-Za-z]*[0-9]*\."
part2 = r"[-1.]/[01.]:([0-9},.]+):[0-9.]+:[0-9.]+:[0-9,.]+"

#for loop
for line in Infile:
        line=line.strip()
        if "##" in line:
                Outfile.write(line + "\n")
        elif "#" in line:
        #need to search through the line for all possible combinations of names (regex string)
	#then replace only the first two sets of information (not the XXX which is unique to each sample)
                newTXstring = re.sub(TxString, "Cf.Sfa.", line)
                newNamesFinal = re.sub(FlString, "Cf.Gai.", newTXstring)
                Outfile.write(newNamesFinal + "\n")
    
        else: #the rest of the data: SNP, allele counts
            part2_SNP = re.sub(part2, r"\1", line)
        #missing data with NA 
            part2NA = re.sub(r"\.","NA",part2_SNP)
        #write to new file 
            Outfile.write(part2NA + '\n')
                



Infile.close()
Outfile.close()
