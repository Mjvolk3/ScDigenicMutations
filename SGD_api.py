# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:36:43 2019

@author: michaelvolk
"""

import requests
import json

def get_go(gene):
    # In URL can use act1 of SGID : S000001855
    #For Manual Entry
    #url = SGD_baseurl + '/locus/act1/go_details'
    SGD_baseurl = "https://yeastgenome.org/backend"
    parameter = '/locus/act1/go_details'
    parameter_lst = parameter.split("/")
    parameter_lst[-2] = gene
    parameter_go = "/".join(parameter_lst)
    print(parameter_go)

    url = SGD_baseurl + parameter_go
    
    response = requests.get(url).json()   
    #"go" dicitonary contains: "go_aspect", "id", "display_name", "go_id"
    go_id = []
    go_aspect = []
    #checking go term total
    acc = 0
    for study in response:
        #print(json.dumps(study["go"], indent = 2))
        #could edit off the GO prefix here
        go_id.append(study["go"]["go_id"])
        go_aspect.append(study["go"]["display_name"])
        acc = acc + 1
    go_id_short = (list(dict.fromkeys(go_id)))
    go_aspect_short = (list(dict.fromkeys(go_aspect)))
    print(json.dumps(go_id_short, indent = 1))
    print(json.dumps(go_aspect_short, indent = 1))
    print(len(go_id_short), len(go_aspect_short))
    
    #change return depending on what is needed/more useful
    return (go_id_short) 

#why is the next line used?
#if __name__ == '__main__':    
    #print_act1_go()
gene = "act1"
get_go(gene)
get_go("ino1")


