#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
# Sample Input: k = 2 arr = [1,4,7,2]
#
# Sample Output: sorted arr = [1,2,4,7] ->  2 - 1 = 1 and 4 - 7 = 3, so we return 1
#

def maxMin(k, arr):
    # Write your code here
    # Sort arr array in descending order and set unfairness to infinity
    arr.sort()
    unfairness = float('inf')
    
    # Loop from 0 for every increments of k elements
    for i in range(len(arr) - k+1):
        
        # If difference between kth and ith elements is less than unfairness, assign as unfairness
        if arr[i+k-1] - arr[i] < unfairness:
            
            unfairness = arr[i+k-1] - arr[i]
            
    return unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
