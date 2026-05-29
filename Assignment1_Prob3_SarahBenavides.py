# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:10:47 2025

@author: sarah
"""

def removeConsecutiveDups(a):
    
    result = [a[0]] if a else []  #initialize result with first element
    
    #looping through list and append non-duplicate elements
    for i in range (1, len(a)):
        
        if a[i] != a[i - 1]:
            
            result.append(a[i])
    
    print(result)
    
    
removeConsecutiveDups([1, 2, 2, 3, 3, 3, 2, 2, 4]) #[1, 2, 3, 2, 4]
removeConsecutiveDups(["a", "a", "b", "b", "a", "c", "c"]) #["a", "b", "a", "c"]
removeConsecutiveDups([7, 7, 7, 7]) #[7]
removeConsecutiveDups([])  #[]
removeConsecutiveDups([1, 2, 3, 4]) #[1, 2, 3, 4]
    
    