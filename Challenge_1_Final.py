import re

vcf = open("Cflorida.vcf", "r")
outfile = open("CorrectedVCF.txt", "w")

#defines regex that will be replaced
TXo=re.compile("[Cc][Ff](07)?\.[Aa]2?\.")
FLo=re.compile('[Cc][Ff]\.[Gg][2Aa][iI]?\.')
#defines what the regex will be replaced by
TXn='Cf.Sfa.'
FLn='Cf.Gai.'

#loop over file
for line in vcf:
    line = line.strip()
    #isolates header
    if line[0]=='#' and line[1]=='#': 
        #writes unchanged header line to file
        outfile.write(line + "\n")
    #isolates line with column headings
    elif line[0]=='#' and line[1] != '#': 
        line=re.sub(TXo,TXn,line)
        line=re.sub(FLo,FLn,line)
        outfile.write(line + "\n")
    #gets into the data
    else:
        #create an empty string
        new_line = ""
        #split each line into columns separated by white space
        col = line.split()
        #loop through each column
        for c in range(len(col)):
            #our regex for data format
            snp_pattern = r'[0-9]+/[0-9]+:([0-9]+,[0-9]+):[0-9]+:.*'
            #here we attempt to grab only the read count per allele
            new_col = re.sub(snp_pattern, r'\1', col[c])
            #if the grabbed string is empty (ie it starts with .), then replace string with N/A
            if new_col[0] == ".":
                new_col = "N/A"
            #Append each new string to the new empty line
            new_line = new_line + "\t" + new_col
        #add new_line to end of the outfile
        outfile.write(new_line + "\n")
        
#Close files
vcf.close()
outfile.close()