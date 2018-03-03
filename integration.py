# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:16:49 2018

@author: Ryan
"""

import sys
import os
import csv
from itertools import filterfalse

# Read in information from data file. Assume Well-formatted.
def readData(name):
    
    file = open(name, "r", encoding="utf8")
    
    return file

def importBasics(basics):
    
    types = {"movie":0, "tvMovie":0}
    newDB = []
    
    basics.readline()
    for line in basics:
        tsv = line.split('\t')
        if tsv[1] not in types:
            continue
        newEntry = [tsv[0], tsv[2], tsv[8].strip()]
        newDB.append(newEntry)
        
    return newDB

def importPrincipals(principals):
    actorDict = {}
    jobList = ['self', 'director', 'actor', 'actress']
    filt_f1 = filterfalse(lambda line: line.startswith('\n'), principals) # Ignores blank lines
    reader = csv.reader(filt_f1, delimiter='\t')
    for row in reader:
        if(row[0] == 'tconst'):
            continue
        if row[0] not in actorDict:
            if row[3] in jobList:
                actorDict[row[0]] = [row[2]]    
        else:
            if row[3] in jobList:
                actorDict[row[0]].append(row[2])
    return actorDict

def mergeDBs(newDB, actorDict):
    for record in newDB:
        if record[0] in actorDict:
            for elem in actorDict[record[0]]:
                record.append(elem)
    return newDB

if __name__ == "__main__":
        
    names = readData("names.tsv")
    principals = readData("titlePrincipals.tsv")
    basics = readData("titleBasics.tsv")
    
    newDB = importBasics(basics)
    actorDict = importPrincipals(principals)
    
    finalDB = mergeDBs(newDB, actorDict)
    
    '''
    newDB = [[tt00001, Blades of Glory, nm00002, nm00004, comedy],[tt000002, "Blazin Saddles", nm23222, comedy],[]]
    for entry in newDB:
       ','.join(entry)
       
       #newDB = ["ttoooo1,Blades of Glory,nm00002", "tt00002,Blazin",]
       
       '\n'.join(newDB)
    '''