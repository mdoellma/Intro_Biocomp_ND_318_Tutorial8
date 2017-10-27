#Exercise 8
#Date: 10-26-2017
#Authors: Janice Love and Melissa Stephens 

#Question 2 

#Open files to read and write
Infile=open("indivIDs.txt","r")
seqFile=  open ("seqFastq.fq", 'r')
Outfile=open("IDseq.fasta","w")

#dictionary for sample IDs 
ID = {}
for line in Infile:
    line = line.strip()
    cols = line.split()
    if cols[0] in ID:
        print ("Duplicate: " + cols[1])
        break
    else:
        ID [cols[0]] = cols[1]

