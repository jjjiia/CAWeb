import os
import csv
import json
#
#if not os.path.exists(directory):
#    os.makedirs(directory)
#

def splitTweetFile(infile,directory):
   
   
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_read = open(infile,"rb")
    row_count = sum(1 for row in file_read)
    print row_count
    
    file_read.seek(0)
    count = 0
    fileName = 0
    newDictionary ={}
    
    
    for row in file_read:
        
        count+=1
        newDictionary["row_"+str(count)] = row.strip(" \r\n").strip("\"").rstrip()
        #print newDictionary
        if count%4000==0:
            
            outfile = directory+"/tweets_"+str(fileName)+".json"
            #print newDictionary
            with open(outfile, 'w') as output:
                json.dump(newDictionary, output)
            count = 0
            fileName +=1
            newDictionary ={}
            
            
        
splitTweetFile("ss13pusb_newTweet.csv","tweets_split")