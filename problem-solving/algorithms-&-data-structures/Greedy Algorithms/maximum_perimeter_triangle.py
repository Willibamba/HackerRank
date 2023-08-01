#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
# Sample Input: sticks = [1,2,3,4,5,10]
#
# Sample Output: Sorted sticks array in descending order[10,5,4,3,2,1] 
#                [10,5,4] = 5 + 4  is less than 10,
#                skip to [5,4,3] = 3 + 4 which is more than 5, we return [3,4,5]
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # Sort the sticks array in descending order
    sticks.sort(reverse=True)
    
    ''' Iterate through the sticks array, 
    return an array of any valid non-degenerate triangle of 3 integers if exists or return [-1] '''
    for i in range(len(sticks)-2):
            
        if (sticks[i+2] + sticks[i+1]) > sticks[i]:
            return [sticks[i+2], sticks[i+1], sticks[i]]
    
    return [-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
