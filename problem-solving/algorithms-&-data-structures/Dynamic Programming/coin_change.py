#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
# Sample Input: n = 4, c = [1, 2, 3]
#
# Sample Output: change = [1, 1, 2, 3, 4]
#                So we return change[-1] = 4
#

def getWays(n, c):
    # Write your code here
    # Create change array and assign the first in value to 1 
    change = [0] * (n+1)
    change[0] = 1
    
    # The logic to calculate the ways to make change
    for i in range(len(c)):
        for j in range(c[i],n+1):
            
            change[j] += change[j-c[i]]
    
    return change[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()