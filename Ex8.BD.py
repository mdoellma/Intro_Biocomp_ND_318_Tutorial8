#Exercise 8, Python question 1

#Open files to read and write

import re
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

texasnames=r"[Cc][Ff](07)?\.[Aa](2)?"
floridanames=r"[Cc][Ff]\.[Gg][Aa2](Ii)?"
regex=r"[01.]/[01.]:([0-9,.]+):[0-9.]+:[0-9.]+:[0-9,.]+"

#loop over file
for Line in vcffile:
    #strip end of line
    Line = Line.strip()
    
    #the header line?
    if "##" in Line: 
    #write unchanged header line to file
        outfile.write(Line + "\n")
    
    elif "#" in Line:
        #standardize sample names with TX and FL regexes
        newnamesTX = re.sub(texasnames,"Cf.Sfa",Line)
        newnamesall = re.sub(floridanames,"Cf.Gai",newnamesTX)
        #write new version of line to file
        outfile.write(newnamesall + "\n")
    
    else:
        #replace full SNP info with allele counts only
        AC=re.sub(regex,r"\1",Line)
        #replace missing data with NA
        ACNA=re.sub(r"\.","NA",AC)
        #write new version of line to new file
        outfile.write(ACNA + "\n")

#Close files
vcffile.close()
outfile.close()