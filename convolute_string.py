"""
Author: Max Randle
Date: 01/04/2019

Generates a result to reflect how similar two strings are.
Slides one string over the other and at each overlap, records matching parts of the string.

SPECIFICALLY FOR ADRESSES

"""

import re

def fuzzyMatch(reference, subject):
    """
    reference - the original string with correct format.
    subject - the string to be tested for matches.
    """
    resultDict = {}
    
    refArr = re.split(' |;|,|\.', reference)

    while "" in refArr:
        refArr.remove("")
    
    for i in refArr:
        resultDict[i] = convoluteString(i, subject)

    print(resultDict)

        
def convoluteString(s1, s2):
    if (s1 == "") or (s2 == ""):
        print("cannot have empty strings")
    
    matchString = []
    if len(s1) > len(s2):
        temp = s1
        s1 = s2
        s2 = temp
    n = len(s1)
    m = len(s2)

    #sliding on
    for i in range(1, n):
        match = matchPartialString(s1[n-i:], s2[0:i])
        if match != "":
            matchString += [match]
        
    #sliding through
    for i in range(0, m - n + 1):
        match = matchPartialString(s1, s2[i:i+n])
        if match != "":
            matchString += [match]

    #sliding off
    for i in range(0, n-1):
        match = matchPartialString(s1[0:n-1-i], s2[m-n+i+1:m-1+1])
        if match != "":
            matchString += [match]
        
    return matchString


def matchPartialString(s1, s2):
    #given two strings of equal length, returns characters that match at the same position in each string
    accuracy = 0.5
    
    matched = 0
    result = ""
    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            matched += 1
        result += s2[i]

    if matched/len(s1) > accuracy:
        return result
    else:
        return ""









