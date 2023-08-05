#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#
# Sample Input: w = [1,2,3,21,7,12,14,21]
#
#Sample Ouput: 1 = [1,2,3], 2 = [7], 3 = [12,14] and 4 = [21,21], so we return 4
#

def toys(w):
    # Write your code here
    # Sort the w array, set weight as value of index 0 plus 4 and containers to 1
    w.sort()
    weight = w[0] + 4
    containers = 1
    
    # Set the index to 1 and start looping till the end
    i = 1
    while i < len(w):
        
        # If the item's weight is greater than weight, increment containers by 1
        # Set weight as the current item's weight plus 4
        if w[i] > weight:
            containers += 1
            weight = w[i] + 4
            
        i += 1    
        
    return containers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
