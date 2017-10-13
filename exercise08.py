import re

vcf = open("Cflorida.vcf", "r")
#outfile = open("Cflorida.txt", "w")

#assign regex to variable name, or compile to variable name


i = 0
#loop over file
for line in vcf:
    line = line.strip()
    i = i + 1
    if i < 10 and line[0] != "#":
        #create an empty string
        new_line = ""
        #split each line into columns separated by white space
        col = line.split()
        #loop through each column
        for c in range(len(col)):
            #our regex for data format
            snp_pattern = r'[0-9]+/[0-9]+:([0-9]+,[0-9]+):[0-9]+:.*'
            #here we attempt to grab only the read count per allele
            new_col = re.sub(pattern, r'\1', col[c])
            #if the grabbed string is empty (ie it starts with .), then replace string with N/A
            if new_col[0] == ".":
                new_col = "N/A"
            #Append each new string to the new empty line
            new_line = new_line + "\t" + new_col
        #add new_line to end of the outfile
        outfile.write(new_line + "\n")
        
#Close files
vcf.close()
#outfile.close()








