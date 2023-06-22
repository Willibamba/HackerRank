#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
sys.setrecursionlimit(1500) # Recursion limit for one hidden case
#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
# A DFS to keep track of visited nodes
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

def journeyToMoon(n, astronaut):
    # Write your code here
    # Graph to group astronauts by county
    countries = {i:set() for i in range(n)}
    for f, l in astronaut:
        countries[f].add(l)
        countries[l].add(f)
    
    # The main logic to calculate the number of valid pairs
    covered = set()
    valid_pairs = 0

    for i in range(n):
        if i not in covered:
            country = dfs(set(), countries, i)
            valid_pairs += len(country) * len(covered)
            
            covered.update(country)
            
    return valid_pairs
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()