#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n                 = 3
#  2. 2D_INTEGER_ARRAY edges    = [[1,2,2][2,3,2][1,3,3]]
#  3. INTEGER start             = 1
#
# Sample Output: = 4 which is 1 -> 2 : 2 -> 3 = 2 + 2 = 4

                
            
def prims(n, edges, start):
    # Write your code here
    # Build the graph
    graph = {i:[] for i in range(1, n+1)}
    for r, l, w in edges:
        graph[r].append([l,w])
        graph[l].append([r,w])
    
    # Sort the graph by the edge weight
    for start in graph:
        graph[start].sort(key = lambda e:e[-1])
    
    visited = set()
    weight = 0
    # The main logic to find the graph minimum overall weight (sum of all edges)
    # among all graphs
    for node in graph:
        
        if node not in visited:
            weight += graph[node][0][1]
            visited.add(graph[node][0][0])     
    
    return weight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()