# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:23:01 2025

@author: sarah
"""

def countAndSay(m, n):
    
    result = []  #creating list
    
    s = m  #number starts from the given m
    
    
    # base cases
    if n == 1:
        return "1"
    if n == 2:
        return "11"
    
    
    for i in range (n):
        
        count = 1   #initialize count of number of matching characters
        temp = ""   #initialize i'th number term to find next term
        
        
        #process previous term to find the next term
        for j in range (1, len(s)):
            
            if (s[j] == s[j - 1]):
                
                count += 1   #count repeated number
            
            #if there's a match, increment count of matching characters
            else:
                temp += str(count) + s[j - 1]  #append count
                count == 1   #reset count

        temp += str(count) + s[-1]  #append last counted group
        result.append(temp)
        s = temp  #update string
        
    return result;


print(countAndSay("1", 4))                
    