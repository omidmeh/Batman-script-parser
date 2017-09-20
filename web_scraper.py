# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:38:29 2017

@author: omidm
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
from unidecode import unidecode

regex = re.compile("[\[\(](.*?)[\]\(]")


def parse_script(wiki_link, destination_list):
    scene_id = 0
    line_number = 0

    page = urlopen(wiki_link)
    soup = BeautifulSoup(page, "lxml")
    title = soup.find("h1", {"id" : "firstHeading"}).get_text()
    
    
    body = soup.find("div", {"class" : "mw-parser-output"})
    scenes = body.find_all("dl")
    for scene in scenes[1:]:
        line_number = 0
        for dd in scene.find_all("dd"):
            text = re.sub(regex, '',dd.get_text())
            text = str(text).encode('ascii', 'ignore').decode()
            text = text.split(":")
            if dd.find("b") == None: 
#                print("--->" , dd.get_text())
                pass
            else :
                if text[0].strip() != '' and text[1].strip() != '':
                    destination_list.append((title, scene_id, line_number, 
                                             text[0].strip(), text[1].strip() ))
                    line_number += 1
                
        scene_id += 1
                
                
###############################################################################
final_list = [] 
                
pages = ["https://en.wikiquote.org/wiki/Batman_(1966_film)",
         "https://en.wikiquote.org/wiki/Batman_Begins",
         "https://en.wikiquote.org/wiki/The_Lego_Batman_Movie"]             

for page in pages:
    parse_script(page, final_list)
    
final_list.append(("default", 0, 0, "nobody", "exit mode" ))
final_list.append(("default", 0, 0, "nobody", "exit mod" ))
final_list.append(("default", 0, 0, "nobody", "exit script mode" ))
final_list.append(("default", 0, 0, "nobody", "exit script mod" ))
final_list.append(("default", 0, 0, "nobody", "exit scripture mode" ))
final_list.append(("default", 0, 0, "nobody", "exit scripture mod" ))
final_list.append(("default", 0, 0, "nobody", "exit" ))
    
library = []
for item in final_list:
    d = dict()
    d["movie"] = item[0]
    d["scene_id"] = item[1]
    d["line_number"] = item[2]
    d["actor"] = item[3]
    d["text"] = item[4]
    d["UID"] = "{0}_{1}_{2}".format(item[0], item[1], item[2] )
    
    library.append(d)
    print(d)
    
    
json_library = json.dumps(library)
with open('.\\data.json', 'w') as outfile:
    json.dump(library, outfile, ensure_ascii=False, sort_keys = True, indent = 3)

#print (json_library)