# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:20:59 2025

@author: sarah
"""

def checking_lists(A, B):
    
    if A == B:
        return "A and B are EQUAL"  
    
    elif not B:
        return "A is SUPERLIST of B"  
    
    elif not A:
        return "A is SUBLIST of B"   
    
    elif len(A) < len(B):
        
        for i in range(len(B) - len(A) + 1):
            
            if B [i:i + len(A)] == A:
                
                return "A is SUBLIST of B"
            
    elif len(A) > len(B):
        
        for i in range(len(A) - len(B) + 1):
            
            if A[i:i + len(B)] == B:
                
                return "A is SUPERLIST of B"
    
        
    return "A and B are UNEQUAL"
    
    
print(checking_lists([], []))  #equal
print(checking_lists([1, 2 , 3], [])) #superlist
print(checking_lists([], [1, 2 , 3])) #sublist
print(checking_lists([1, 2, 3], [1, 2, 3, 4, 5])) #sublist
print(checking_lists([3, 4, 5], [1, 2, 3, 4, 5]))  #sublist
print(checking_lists([3, 4], [1, 2, 3, 4, 5]))  #sublist
print(checking_lists([1, 2, 3], [1, 2, 3]))  #equal
print(checking_lists([1, 2, 3, 4, 5], [2, 3, 4]))  #superlist
print(checking_lists([1, 2, 4], [1, 2, 3, 4, 5]))  #unequal
    
    