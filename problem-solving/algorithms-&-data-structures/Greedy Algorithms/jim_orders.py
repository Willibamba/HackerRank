#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#
# Sample Input: orders = [[8,3],[5,6],[6,2],[2,3],[4,3]]
#
# Sample Output: serve_time = [5,7,8,11,11] -> customers = [4,5,3,1,2]

def jimOrders(orders):
    # Write your code here
    ''' Loop orders array, sum the values (prep[0], prep[1]) as serve time,
        save it in delevery dictionary as keys and indexes as values in list '''
    delivery = {}
    for i, prep in enumerate(orders):
        serve_time = sum(prep)
        if serve_time in delivery.keys():
            delivery[serve_time].append(i+1)
        else:
            delivery[serve_time] = [i+1] 
    
    # Sort the keys in delivery in ascending order as a list
    serve_time = list(sorted(delivery.keys()))
    
    ''' Loop sorted serve time list in delivery keys for each customer, 
        add to customers array and return customers array '''
    customers = []      
    for time in serve_time:
        for customer in delivery[time]:
            customers.append(customer)
        
    return customers   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
        
    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
