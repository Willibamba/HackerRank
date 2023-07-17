#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crabGraphs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n = 1
#  2. INTEGER t = 8 2 7
#  3. 2D_INTEGER_ARRAY graph = [[1,4][2,4][3, 4][5,4][5,8][5,7][5,6]]
#
# Output Sample: crabs = {4: [1,2,3,5], 5: [4,6,7,8]} 
#                nodes = {1,2,4,5,7,8} 
#                Answer = 6

def crabGraphs(n, t, graph):
    # Write your code here
    # Build graph
    crabs = {i:[] for i in range(1, n+1)}
    for parent, child in graph:
        crabs[parent].append(child)
        crabs[child].append(parent)
    print(crabs)
    # Main logic to calculate the maximum number of vertices of sub-graph of crabs-graph 
    node = set()
    for crab in crabs:
        
        if crab not in node and len(crabs[crab]) >= t:
            node.add(crab)
            
    for crab in sorted(crabs, key = lambda s:len(crabs[s]), reverse=True):        
        count = 0
        for feature in crabs[crab]:
            
            if feature not in node and count < t:
                node.add(feature)
                count += 1
    
    return len(node)       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()
