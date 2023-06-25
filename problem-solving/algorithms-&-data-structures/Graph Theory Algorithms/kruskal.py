#!/bin/python3

import math
import os
import random
import re
import sys
# Set recursion limit for one test case 
sys.setrecursionlimit(1500)

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
# Sample Input:  g_nodes = 4 6
#               g_from = [1,1,4,2,3,3]
#               g_to = [2,3,1,4,2,4]
#               g_weight = [5,3,6,7,4,5]
#
# Sample Output: 12

# Helper functions to find the set and parent node
def findSet(parent, i):
    if parent[i]  == i:
        return i
    return findSet(parent, parent[i])

def union(parent, u, v):
    parent[u] = v
    return parent 

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    # Arrays to keep track of parent and edges sorted by weight
    parent = [i for i in range(g_nodes+1)]
    edges = [[g_from[i], g_to[i], g_weight[i]] for i in range(len(g_from))]
    edges.sort(key = lambda e:e[-1])
    # The main logic to find the minimum overall weight
    weight = 0
    for u, v, wt in edges:
        ux = findSet(parent, u)
        vx = findSet(parent, v)
        if ux != vx:
            parent = union(parent, ux, vx)
            weight += wt
            print(parent, ux, vx)
    
    return weight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))
    fptr.close()
