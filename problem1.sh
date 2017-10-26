#Exercise 8, Python question 1
#10/13/17, MMD

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

#loop over file
for :#look at old code to see how you looped over a file
    #strip end of line
    if : #how can you tell if this is the header line?
        #write unchanged header line to file
    elif : #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        #write new version of line to file
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files


vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

r1 = r"[Cc][Ff][0-9]?\.[Aa]2?\.[0-9]{3}"
r2 = r"[Cc][Ff]\.[Gg].\.[0-9]{3}"

for Line in vcffile:
	Line=Line.strip()
	if '##' in Line:
		outfile.write(Line + "\n)
	elif 'CHROM' in Line:
		if r1 in Line:
			re.sub(Cf.Sfa