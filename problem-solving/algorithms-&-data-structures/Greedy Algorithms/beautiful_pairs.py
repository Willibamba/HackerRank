#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#
# Sample Input: A = [1, 2, 3, 4] and B = [1, 2, 3, 3]
#
# Sample Output: 4
#

def beautifulPairs(A, B):
    # Write your code here
    counter = 0
    ''' Make the A array as set and iterate through through it
    Increment the counter with any of the two arrays (A or B) with minimum count of occurence of the number '''
    for num in set(A):
        
        counter += min(A.count(num), B.count(num))
    
    if counter < len(A):
        return counter + 1
    
    return counter - 1            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
