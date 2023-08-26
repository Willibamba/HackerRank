#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#
# Sample Input: n = 4, k = 3, x = 2
#
# Sample Output: 3

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    # Create arr array, modulo and start value 
    arr = [0,1]
    mod = (10**9)+7
    st = k-1 
    
    # Main logic to calculate the number of ways to construct distinct consecutive elements of the array
    for i in range(2, n):
        step = st - arr[len(arr)-1] 
        arr.append(step % mod)
        st = (st * (k-1)) % mod
     
    ways = arr[len(arr)-1] 
    
    if x == 1:
        if n % 2 == 0:
            ways -= 1
        else:
            ways += 1
            
    return ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()