#Exercise 8
#Date: 10-26-2017
#Authors: Janice Love and Melissa Stephens 

#Question 2 


import pandas as pd 

#Open files to read and write
Infile=open("indivIDs.txt","r")
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

Infile.close()



barcode = r"[ACGT]{8}(AATTC)[ACGT]*." #regex for barcode, cut site, rest of sequence  
seqFile=  open ("seqFastq.fq", 'r')

while line != " ":
    if "#" in line: #header 
        line = line.strip()
        Outfile.write(line + "\n")
    elif barcode in line:
        
        
    
