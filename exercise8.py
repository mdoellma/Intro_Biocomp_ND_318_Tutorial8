#### Tutorial 8
# Set wd for Brittni: 
os.chdir('/Users/brittnibertolet/Desktop/bcTutorials/Intro_Biocomp_ND_318_Tutorial8/')


import re

vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

# Set variables of regular expressions
r1=r"[Cc][Ff][0-9]?/.[Aa][2]?/.([0-9]{3})"
r2=r"[Cc][Ff][0-9]?/.[Gg].?/.([0-9]{3})"


#loop over file
for Line in vcffile:
    Line = Line.strip() #strip end of line
    if '##' in Line: # how can you tell if this is the header line?
        outfile.write(Line + "\n") # write unchanged header line to file
    elif '#CHROM' in Line: #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        outfile.write(Line + "\n") 
    else:
        Line_v2=re.sub(r1, "Cf.Sfa./1", Line)
        Line_v3=re.sub(r2, "Cf.Gai./1", Line_v2)
        #write new version of line to file
        outfile.write(Line_v3 + "\n") 
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files



