#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k   e.g. k = 2
#  2. INTEGER_ARRAY arr e.g. arr = [1, 5, 3, 4, 2]
#  Sample Output = 3
#  Explanation: There are 3 pairs of integers in the set with a difference of 2:
#               [5,3], [4,2] and [3,1]
#

def pairs(k, arr):
    # Write your code here
    # Sort the arr in descending order and set counter to 0
    arr.sort(reverse=True)
    counter = 0
    
    # Iterate through the array arr for the pairs, 
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # once the difference is greater than k, break from the loop
            if arr[i] - arr[j] > k:
                break
            # if the difference is equal to k, increment the counter by 1
            if arr[i] - arr[j] == k:
                counter += 1
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
