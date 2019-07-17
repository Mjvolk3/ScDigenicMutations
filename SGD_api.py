# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:36:43 2019

@author: michaelvolk
"""

import requests
import json

def get_go(gene):
    #In URL can use act1 of SGID : S000001855
    #For Manual Entry
    #url = SGD_baseurl + '/locus/act1/go_details'
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/act1/go_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene
    parameter_go = "/".join(parameter_lst)
    #print(parameter_go)

    url = SGD_baseurl + parameter_go
    
    response = requests.get(url).json()   
    #"go" dicitonary contains: "go_aspect", "id", "display_name", "go_id"
    
    go_temp = []
    go_tot = []

    #checking go term total
    for exp in response:
        #print(json.dumps(study["go"], indent = 2))
        #could edit off the GO prefix here
        go_temp.append(exp["go"]["go_aspect"]) 
        go_temp.append(exp["go"]["go_id"])
        go_temp.append(exp["go"]["display_name"])   
            
        if go_temp not in go_tot:
            go_tot.append(go_temp)
            
        go_temp = []
        
    return (go_tot) 

#why is the next line used? -- FROM ORIGINAL .py
#if __name__ == '__main__':    
    #print_act1_go()

#Uncomment to see example
#gene = "act1"
#get_go(gene)
#print(json.dumps(get_go("aft2"), indent = 2))


