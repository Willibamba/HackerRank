#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kMarsh' function below.
#
# The function accepts STRING_ARRAY grid as parameter.
#
# Input Sample: grid = ["....", "..x.", "..x.", "x..."]
#
# Sample Output: longest perimeter = 10 -> 2 * 1 + 2 * (4 - 0)
#  

def kMarsh(grid):
    # Write your code here
    height, width = len(grid), len(grid[0])
    land = {}
    perimeter = 0

    # Build the land dictionary with False value and 0
    for i in range(width-1):
        for j in range(i+1, width):
            land[i,j] = [False, 0]
            
    # For each row initialise connect with True value and turn to False value if condition is met 
    for k in range(0, height):
        for i in range(width-1):
            connect = True
            if grid[k][i] == "x":
                connect = False
            # For each column check the conditions, apply values and calculate the longest perimeter    
            for j in range(i+1, width):
                if grid[k][j] == "x":
                    connect = False
                if land[i,j][0] == True:
                    if grid[k][i] != "x" and grid[k][j] != "x":
                        land[i,j][1] += 1
                        if connect ==  True:
                            area = 2 * land[i,j][1] + 2 * (j - i)
                            
                            if perimeter < area:
                                perimeter = area
                    else:
                        land[i,j][0] = False
                        land[i,j][1] = 0
                else:
                    if connect == True:
                        land[i,j] = [True, 0]

    # If perimeter is greater than 0, print it else print "impossible"                
    if perimeter > 0:
        print(perimeter)
        return
    print("impossible")
        
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    grid = []

    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)

    kMarsh(grid)
