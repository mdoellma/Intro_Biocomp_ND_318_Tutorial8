#### Tutorial 8
# Set wd for Brittni: 
#os.chdir('/Users/brittnibertolet/Desktop/bcTutorials/Intro_Biocomp_ND_318_Tutorial8/')


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
        print(Line) # write unchanged header line to file
    elif '#' in Line: #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        Line=re.sub(r1, "Cf.Sfa./1", Line)
        Line=re.sub(r2, "Cf.Gai./1", Line)
        #write new version of line to file
        print(Line)
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files



