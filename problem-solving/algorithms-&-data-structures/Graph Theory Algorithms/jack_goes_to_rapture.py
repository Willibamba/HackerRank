#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *
#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes. = 
# 2. The number of edges is <name>_edges. 
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
# Input Sample:
#               g_nodes = 4
#               g_from  = [1,1,2,3]
#               g_to    = [2,3,4,4]
#               g_weight = [20,5,30,40]
# Output Sample:
#        Travel from station 1->2 = 20, 2->4 = (30 - 20) = 10 
#        Travel from station 1->3 = 5, 3->4 = (40 - 5) = 35 
#        The lowest fare from between station 1 to 4 is 1->2->4 = (20 + 10) = 30

 
def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    # graph building logic
    graph = {i:[] for i in range(1, g_nodes+1)}
    for i in range(len(g_from)):
        graph[g_from[i]].append([g_to[i], g_weight[i]])
        #graph[g_to[i]].append([g_from[i], g_weight[i]])
    
    distance = [float("inf")] * (g_nodes + 1)
    distance[1] = 0 
    node = [[0,1]]
    visited = [False] * (g_nodes + 1)
    
    # The main logic to calculate the lowest fare from staion 1 to n (g_nodes)
    while node:
        cumm_cost, station_from = heappop(node)
        
        if visited[station_from]:
            continue 
        visited[station_from] = True
        for station_to, cost in graph[station_from]:
            
            if distance[station_to] > cumm_cost + max(0, cost - cumm_cost):
                distance[station_to] = cumm_cost + max(0, cost - cumm_cost)
                heappush(node, (distance[station_to], station_to))
    
    if distance[-1] != float("inf"):
        print(distance[-1])  
    else:
        print('NO PATH EXISTS')
    
          
            

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
