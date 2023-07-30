#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
# Sample Input: grid = ["abc", "ade", "efg"]
#
# Sample Output: String either YES or NO
#                The rows are already in alphabetical order. 
#                Columns a a e, b d f and c e g are also in alphabetical order, 
#                So the answer would be YES. 
#                Only elements within the same row can be rearranged. They cannot 
#                be moved to a different row.
#

def gridChallenge(grid):
    # Write your code here
    # An array to keep track of the grid in order
    check = ["a" for i in range(len(grid[0]))]
    
    # Iterate through the grid and covert row to list and sort in ascending order
    for row in grid:
        row = sorted(list(row))
        
        for i in range( len(row)):
            # if current index of check value is greater than current index of row value, return NO 
            if check[i] > row[i]:
                return "NO"
            # Else, change the value of current index of check to value of current of row   
            check[i] = row[i]
                
    return "YES"        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()