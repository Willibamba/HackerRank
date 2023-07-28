#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Sample Input: [3, -7, 0]
# Sample Out: |3--7| -> 10, |3-0| -> 3, |-7-0| -> 7
#             The smallest of these absolute differences is 3
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    # Sort the arr and assign minimum difference
    arr.sort()
    min_diff = float("inf") 
    
    # Iterate through the array and assign current index minus 1 as j
    for i in range(len(arr)):
            j = i - 1  
            
            # If true, assign minimum difference as absolute difference     
            if abs(arr[i] - arr[j]) < min_diff:
                min_diff = abs(arr[i] - arr[j])
    
    return min_diff
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()