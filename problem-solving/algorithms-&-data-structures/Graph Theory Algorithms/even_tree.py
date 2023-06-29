#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.

# Complete the evenForest function in the editor below. It should return an integer as described.

# evenForest has the following parameter(s):

# t_nodes: the number of nodes in the tree              = 4
# t_edges: the number of undirected edges in the tree   = 3
# t_from: start nodes for each edge                     = [1,1,3]
# t_to: end nodes for each edge, (Match by index to t_from = [2,3,4]
#
# Output Sample: 1 = [1,3]


def evenForest(t_nodes, t_edges, t_from, t_to):
    # Graph for the nodes
    nodes =[[] for _ in range(t_nodes)]
    for r, l in zip(t_from,t_to):
        nodes[l-1].append(r-1)
        
    # A recursive DFS   
    def dfs(node,):
        nonlocal result
        v=1
        for child in nodes[node]:
            v+=dfs(child)
        print(v)
        if v % 2 == 0 and node != 0:
         result +=1
        return v
    
    result = 0
    dfs(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
