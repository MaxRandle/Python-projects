"""
Author: Max Randle

fuzzy string match V2

match two adresses
"""

import math
import re

def fuzzy(address, subject):
    """
    address - the known address
    subject - the string to be tested for a match to the address
    """

    resultDict = {}

    address.lower()
    subject.lower()    
    
    #split up the address
    addArr = re.split(' |;|,|\.|/', address)
    while "" in addArr:
        addArr.remove("")

    #split up the subject
    subArr = re.split(' |;|,|\.|/', subject)
    while "" in subArr:
        subArr.remove("")

    for i in addArr:
        resultDict[i] = []
        for j in subArr:
            if match(i,j) == True:
                resultDict[i] += [j]

    print(resultDict)

def match(s1, s2):
    #returns a bool of whether two things match
    threshold = math.floor(min(len(s1), len(s2))/2)
    if LD(s1, s2) <= threshold:
        return True
    else:
        return False

def LD(s, t):
    #Levenshtein Distance Recursive Algorithm
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res


