#### Tutorial 8

import re

vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")


# [Cc][Ff][0-9]?/.[Aa][2]?/.[0-9]{3}