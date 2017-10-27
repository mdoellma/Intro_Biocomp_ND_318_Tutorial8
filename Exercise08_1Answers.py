# Exercise 8
# Author: Kathleen Nicholson
# This code is used to create a standard naming system for sequence information and moves all allele counts
#   to an output file called CfloridaCounts.txt.
import re


# This opens the files to read them and write.
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

# Assigning regexes to variables
Texas=(r"[Cc][Ff](07)?\.[Aa]2?")
Florida=(r"[Cc][Ff]\.(G2|GAI|gai)")
SNPs=(r"[01.]/[01.]:([0-9,.]+):[0-9.]+:[0-9.]+:[0-9,.]+")


# This is a for loop which loops over the file being read and places the output in a .txt file
for line in vcffile :
# This strips the lines of '\n' at the ends.
    line=line.strip()
    # This tests to see if '##' is in the beginning of the line and if it exists, it is written to the outfile "CfloridaCounts.txt"
    if '##' in line :
            outfile.write(line + "\n")
    elif "#" in line : #This takes the line beginning with # and runs the code below.
    # This replaces sample names with standardized TX and FL regexes
        newnamesTX = re.sub(Texas, "Cf.Sfa", line)
        allnewnames = re.sub(Florida, "Cf.Gai", newnamesTX)
        outfile.write(allnewnames + "\n")
        # This writes the new version of the line to the output file
    else: # This runs through the actual data within the file.
                # This replaces the full SNP information with allele counts only
                AC = re.sub(SNPs, r"\1", line)
                # This replaces any missing data (with periods) with NA
                ACNA = re.sub(r"\.", "NA", AC)
                # This writes the new version of the allele counts to new file
                outfile.write(ACNA + "\n")
      
#Close files
vcffile.close()
outfile.close()