# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:31:21 2025

@author: sarah
"""

#values

prior = 0.3846  #answer from Q1
true_positive_rate = 0.95
false_positive_rate = 0.08

certainty = 0.99

#counting number of positive tests
positive_tests = 0

while prior < certainty:
    
    #Bayesian Theorem
    numerator = true_positive_rate * prior
    demoninator = numerator + false_positive_rate * (1 - prior)
    posterior = numerator / demoninator
    
    #updating prior for next iteration
    prior = posterior
    positive_tests += 1
    
print(f"Number of positive tests in a row needed to reach 99% certainty: {positive_tests}")

# How many positive test results in a row would be needed to reach this level of certainty?
# 3


# Q4.1. If we don’t know the dictator’s mood, how much would the amount of free food
# (A) tell us about the number of holidays (B)? Why?

# If we don't know the dictator's mood, the amount of free food (A) would tell us a lot 
# about the number of holidays (B). This is because both free food and holidays are 
# connected through the dictator's mood. If there's a lot of free food, it hints that 
# the dictator is probably happy which makes holidays more likely too. So, seeing more 
# free food would make us believe there will be more holidays, even if we don't know
# his mood directly.


# Q4.2. If we know the dictator is happy, how much would the amount of free food (A)
# tell us about the number of holidays (B)? Why?

# If we already know the dictator is happy, then the amount of free food (A) would not
# tell us much more about the number of holidays (B). Since the mood (happy) already
# explains why there could be lots of holidays, looking at the free food doesn't add 
# new information. Once we know the mood, free food and holidays become independent
# of each other. 

