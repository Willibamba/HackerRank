#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
# Sample Input: k = 2, arr = [0,1,1,1,1,0]
#
# Sample Output: Cities arr[1], arr[2], arr[3] and arr[4] are suitable for power plants
#                City arr[1] for cities arr[0] through to arr[3] = 1 power plant
#                City arr[4] for cities arr[4] and arr[5] = 1 power plant
#                return 2 power plants
#

def pylons(k, arr):
    # Write your code here
    # Set starting distance to k minus 1 and power plants to 0
    distance =  k-1
    last_distance = -1
    plants = 0
    
    # Iterate for suitable distribution plants 
    while distance < len(arr):
        # if true, increment plants to 1, set last distance as current distance
        if arr[distance] == 1:
            plants += 1
            last_distance = distance
            
            # If distance plus k is beyond the list, break
            if (distance + k) >= len(arr):
                break
            # If double of k minus 1 plus current distance is within list, set it as distance or set end of the list as distance
            elif (2 * k-1) + distance < len(arr)-1:
                distance = (2 * k-1) + distance
            else:
                distance = len(arr) - 1
                
        # if true decrement by one and if distance is last distance return -1
        elif arr[distance] == 0:
            distance -= 1
            if distance == last_distance:
                return -1     
               
    return plants

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
