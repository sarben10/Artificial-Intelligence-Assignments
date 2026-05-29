# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:58:21 2025

@author: sarah
"""

import numpy as np
import matplotlib.pyplot as plt

# Objective function for the one max problem (maximize the sum of bits)
def onemax(x):
    return np.sum(x)  # Sum of bits represents the fitness of the individual

# Selection function for tournament selection
def selection(pop, scores, k=3):
    selected_indices = np.random.randint(0, len(pop), k)
    best_index = selected_indices[0]
    for ix in selected_indices[1:]:
        if scores[ix] > scores[best_index]:
            best_index = ix
    return pop[best_index]

# Crossover function to create two children from two parents
def crossover(p1, p2, r_cross):
    c1, c2 = np.copy(p1), np.copy(p2)
    if np.random.rand() < r_cross:                    # Question 1
    
        # original code
        pt = np.random.randint(1, len(p1)-1)
        c1[:pt], c2[:pt] = p2[:pt], p1[:pt]
        
        pt1, pt2 = np.random.randint(1, len(p1)-1, 2)
        pt1, pt2 = min(pt1, pt2), max(pt1, pt2)  # ensure correct order
        c1[pt1:pt2], c2[pt1: pt2] = p2[pt1:pt2], p1[pt1:pt2]  # swap segments
    return [c1, c2]


# Mutation operator
def mutation(bitstring, r_mut):                     # Question 2
    index = np.random.randint(0, len(bitstring))  # to ensure at least one bit is flipped 
    bitstring[index] = 1 - bitstring[index]
    for i in range(len(bitstring)):
        if np.random.rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]           


# Genetic algorithm with visualization
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    # Initial population of random bitstrings
    pop = np.random.randint(0, 2, (n_pop, n_bits))  # 0 is the start and 2 is the finish, n_pop is # of population, n_bits is # of bits
    best, best_fitness = None, float('-inf')
    best_solutions = []
    avg_fitness = []

    for gen in range(n_iter):  # n_iter basically # of generations
        scores = np.array([objective(c) for c in pop])  # scores in numpy array; objective is function onemax, onemax returns sum of fitness | c is place holder, calling onemax function | ex my_list = [1, 2, 3, 4] when you write [c**2 for c in my_list] you square things in list
        avg_fitness.append(np.mean(scores)) # avg fitness of first generation and add to list
        
        for i in range(n_pop):
            if scores[i] > best_fitness:
                best, best_fitness = pop[i], scores[i]  # within population we look at best fitness of best individual to see when to stop
        
        best_solutions.append(best_fitness)

        selected = np.array([selection(pop, scores) for _ in range(n_pop)])  # 
        children = []
        for i in range(0, n_pop, 2):
            p1, p2 = selected[i], selected[i+1]
            for c in crossover(p1, p2, r_cross):  # performing crossover
                mutation(c, r_mut)  # after you crossover mutation happens
                children.append(c)
        pop = np.array(children)  # add children to population

    return [best, best_fitness], best_solutions, avg_fitness

# Define parameters
n_iter = 100
n_bits = 20
n_pop = 100
r_cross = 0.9
r_mut = 0  #1.0 / float(n_bits)


# Question 3

# Run the genetic algorithm (original and modified)
(original_best, original_best_fitness), original_best_solutions, original_avg_fitness = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut) 
(modified_best, modified_best_fitness), modified_best_solutions, modified_avg_fitness = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)

# Plotting
plt.figure(figsize=(12, 6))

# Plot best solutions
plt.subplot(1, 2, 1)
plt.plot(original_best_solutions, label = "Original GA Best Fitness", color = 'red', linestyle = "dashed")
plt.plot(modified_best_solutions, label = "Modified GA Best Fitness", color = 'blue')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Best Fitness Over Generations")
plt.legend()
plt.grid(True)

#import matplotlib.ticker as ticker

# Plot average fitness
plt.subplot(1, 2, 2)
plt.plot(original_avg_fitness, label='Original GA Avg Fitness', color = 'red', linestyle = "dashed")
plt.plot(modified_avg_fitness, label = 'Modified GA Avg Fitness',color = 'blue')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Average Fitness Over Generations')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print('Done!')
print(f'Original GA Best Solution: f({original_best}) = {original_best_fitness:.6f}')
print(f'Modified GA Best Solution: f({modified_best}) = {modified_best_fitness:.6f}')

# Question 4:
    # In the Best Fitness Over Generations graph, the original GA and modified GA reach maximum fitness roughly around the same time before plateauing.
    # In the Avg Fitness Over Generations graph, the modified GA reaches a higher fitness level than the original GA. Both the original GA and modified GA fluctuate over the increased number of generations 