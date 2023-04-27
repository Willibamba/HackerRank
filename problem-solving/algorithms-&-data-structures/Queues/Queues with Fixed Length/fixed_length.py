#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    minimums = []
    
    for query in queries:
        
        minimum = maximum = max(arr[:query])
        i = 1
        while i <= len(arr)-query:
             
            if arr[i-1] == maximum:
               subarrays = max(arr[i:i+query])
            else:
                subarrays = max(maximum, arr[i]) 
                
            minimum = min(minimum, subarrays)
            maximum = subarrays
            i += 1
        
        minimums.append(minimum)
        
    return minimums
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
