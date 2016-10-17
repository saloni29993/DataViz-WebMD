import difflib as dl
import json
import re

def extractfrquency():
    file_read=open('ScrapedData/diseases.txt','r')
    diseaselist=[]
    lines=file_read.readlines()
    for line in lines:
        line=re.split('\(',line)
        diseaselist.append(str(line[0]).strip('\n\t\r'))
    
    filewriter = open("diseaseYear.csv", "w+")
    
    newline = ""
    jdata = json.loads(open ('dataset/webmd-question.json').read())
    for  q in jdata:
        med=dl.get_close_matches(q['questionTitle'],diseaselist,10,0.7)
        if len(med) !=0 and len(q['questionPostDate']) != 0:
            write_string = str(med[0]).strip() + "," + q['questionPostDate'].split("-")[0]
            filewriter.write(newline + write_string)
            print write_string
            newline = "\n"
            
    
    
extractfrquency()
    