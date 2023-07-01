#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders = [[32, 62], [42, 68], [12, 98]]
#  2. 2D_INTEGER_ARRAY snakes  = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
#
# Output sample:    3 =  die roll of a 5 and a 6 to land at ladder 12 climb to 98 
#                        and  a roll of 2 to land at 100
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    # Build a graph
    graph = {}
    for l in ladders:
        graph[l[0]] = l[1]
    for s in snakes:
        graph[s[0]] = s[1]
    
    visited = set([1])
    queue = [1]
    rolls = {}
    # The main logic to find find the least number of rolls to reach 100, if there is such rolls
    while queue:
        current = queue.pop(0)
        
        for i in range(1, 7):
            neighbor = graph.get(current + i, current + i)
            
            if neighbor not in visited:
                rolls[neighbor] = rolls.get(current, 0) + 1
                print(rolls[neighbor])
                visited.add(neighbor)
                queue.append(neighbor)
                
            if neighbor == 100:
                return rolls[neighbor]
    # If no such rolls of a die exists, return -1         
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()