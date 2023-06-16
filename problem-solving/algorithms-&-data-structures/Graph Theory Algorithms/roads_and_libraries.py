#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n    e.g. n = 3
#  2. INTEGER c_lib     e.g. c_lib = 6
#  3. INTEGER c_road    e.g. c_road = 1
#  4. 2D_INTEGER_ARRAY cities e.g. cities = [[1,2], [1,3], [1,4]]
#
# Output: minimal cost = 15
#

# A DFS function to keep track of visitted node(s)
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib <= c_road:
        return c_lib * n
    
    # Build a graph to connect cities using dictionary
    graph = defaultdict(list)
    for begin, end in cities:
        graph[begin].append(end)
        graph[end].append(begin)
    
    print(graph)
    # A set for covered cities
    covered = set()
    cost = 0
    
    # The main logic to calculate the minimal cost for building to connect cities
    for node in range(1, n+1):
        if node not in covered:
            city_conn = dfs(set(), graph, node)
            
            to_build = len(city_conn)-1
            cost += to_build * c_road
            cost += c_lib
            
            for city in city_conn:
                covered.add(city)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
