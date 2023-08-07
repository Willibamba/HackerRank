#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
# Sample Input: k = 1, arr = [1,2,3,4]
#
# Sample Output: arr = [4,2,3,1]
#

def largestPermutation(k, arr):
    # Write your code here
    # While k is greater than 0 keep looping the arr array
    for i in range(len(arr)):
        if k == 0:
            break
            
        # Find the highest value and it's index from next index to the last index
        # If the highest value is greater than the current value swap them and decrement k by 1 
        highest = max(arr[i:])
        j = arr.index(max(arr[i:]))
        if arr[i] != highest:
            arr[j], arr[i] = arr[i], highest
            arr[i] = highest
            k -= 1
            
    return arr                 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
