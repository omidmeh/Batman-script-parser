# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:52:38 2017

@author: omidm
"""


from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from urllib.request import urlopen
import re




transcripts = [("Batmen Begins", 'batman_begins.txt')]




def file_parser(transcripts):
    dialogs = []
    meta = []
    
    regex = re.compile("\[(.*?)\]")
    for movie_name, file_address in transcripts:
        with open(file_address) as f:
            for l in f:
                result = re.sub(regex, '',l).strip('\n')
                
                if result != '' and result[0] != '[':
                    to_add = result.split(':', 1)
            #        print (to_add)
                    assert(len(to_add) == 2)
                    dialogs.append(to_add[1].strip())
                    meta.append((movie_name, to_add[0].strip()))
    return dialogs, meta


dialogs, meta = file_parser(transcripts)

y = process.extractOne("how do you no my name", 
                       dialogs, scorer=fuzz.partial_ratio)

idx = dialogs.index(y[0])
print(y)
print(idx, meta[idx])
