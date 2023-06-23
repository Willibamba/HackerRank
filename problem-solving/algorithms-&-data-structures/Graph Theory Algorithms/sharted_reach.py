#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    # Write your code here
    # Creating a graph with defaultdict
    nodes = defaultdict(list)
    for i, j in edges:
        nodes[i].append(j)
        nodes[j].append(i)
    
    # Initialize all the distances to nodes with -1 except the first node as 0
    distances = [-1] * n
    distances[s-1] = 0
    
    # Use deque(double-ended queue) to implement BFS traversal 
    # starting from the given node and enqueue it
    queue = deque([s])
    while queue:
        node = queue.popleft()
        for neighbour in nodes[node]:
            if distances[neighbour-1] == -1:
                distances[neighbour-1] = distances[node-1] + 6
                
                queue.append(neighbour)
                
    distances.pop(s-1)  
    return distances 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
