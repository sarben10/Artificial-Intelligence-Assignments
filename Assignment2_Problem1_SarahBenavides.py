# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:20:46 2025

@author: sarah
"""

import numpy as np


def original_grid(size = 10):
    
    # creating random np array of 0s and 1s
    return np.random.randint(0, 2, size = (10, 10))

def live_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),   # defining postions of possible neighbors
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    # calculating sum of values of neighbors that are within range of grid
    return sum(grid [x + dx, y + dy] for dx, dy in neighbors if 0 <= x + dx < grid.shape[0] and 0 <= y + dy < grid.shape[1])  
        
def updating_grid(grid):
    new_grid = grid.copy()  #creating copy of original grid
    
    # iterating over grid
    for i in range(grid.shape[0]):   # number of rows
        
        for j in range(grid.shape[1]):  #number of columns
            living_neighbors = live_neighbors(grid, i, j)  # counting live neighbors
            
            # live cell with fewer than 2 and more than 3 live neighbors dies
            if grid[i, j] == 1 and (living_neighbors < 2 or living_neighbors > 3):
                new_grid[i, j] = 0
            
            # dead cell with exactly 3 neighbors becomes alive
            elif grid[i, j] == 0 and living_neighbors == 3:
                new_grid[i, j] = 1
    
    return new_grid

# simulate for 5 times
def five_iterations(iterations = 5, size = 10):
    grid = original_grid(size)
    print("Original Grid: ")
    print(grid)
    
    for step in range(iterations):
        grid = updating_grid(grid)
        print(f"\nIteration {step + 1}: ")
        print(grid)
        
five_iterations()
    
    