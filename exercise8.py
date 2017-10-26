#### Tutorial 8
# Set wd for Brittni: 
os.chdir('/Users/brittnibertolet/Desktop/bcTutorials/Intro_Biocomp_ND_318_Tutorial8/')


import re

vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

# Set variables of regular expressions
reg1=r"[Cc].{1,3}\.[a|A][0-9]?\.([0-9]{3})"
reg2=r"[Cc].{1,3}\.[g|G].{1,2}\.([0-9]{3})"
reg3=r"[0|1]\/[0|1]\:([0-9]{1,3}\,[0-9]{1,3})\:[0-9]{1,3}\:[0-9]{1,3}\:[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}"
reg4=r"\.\/\.\:\.\:\.\:\.\:\."


#loop over file
for Line in vcffile:
    Line = Line.strip() #strip end of line
    if '##' in Line: # how can you tell if this is the header line?
        outfile.write(Line + "\n") # write unchanged header line to file
    elif '#CHROM' in Line: #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        Line_v2=re.sub(reg1, "Cf.Sfa.\g<1>", Line)
        Line_v3=re.sub(reg2, "Cf.Gai.\g<1>", Line_v2)
        #write new version of line to file
        outfile.write(Line_v3 + "\n") 
    else: #now you're in the data
        Line_v2=re.sub(reg3, "\g<1>", Line)#replace full SNP info with allele counts only
        Line_v3=re.sub(reg4, "NA", Line_v2)
        #replace missing data with NA
        #write new version of line to new file
        outfile.write(Line_v3 + "\n")
outfile.close() #Close files
vcffile.close()




