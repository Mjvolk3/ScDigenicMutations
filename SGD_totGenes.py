# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:44:13 2019

@author: Michael Volk
"""
import json
from SGD_api import get_go

#print(get_go("S000004660"))

#common names, but more ambiguous, and not necessarily linked to SGD
lst_gene_des = [] 
#SGD ref will likely be more useful since GO is sourced from SGD
lst_SGD_ref = []

#count for getting passed prefix to data
count = 0 
with open ("yeastUniprot_v2.txt", 'r') as file:
    for line in file:
        #print ("\n",count)
        count = count + 1
        #print (line.split())
        
        #line numbers should fix later
        if count > 58 :
            lst_gene_des.append(line.split()[0])
            
            for i in line.split():
                #using SGD X-ref becuase it is the easiest data to grab from file
                if (i[:4]) == "S000":
                    lst_SGD_ref.append(i)
                    print(lst_SGD_ref[-1])


#Problem is down here somewhere
gene_go = {}    

for i in (lst_SGD_ref):
    gene_go[i] = get_go(i)
    #print(json.dumps(gene_go, indent = 2))
#
#with open ('gene_go.txt', 'w') as outfile:
#    json.dump(gene_go, outfile)
    