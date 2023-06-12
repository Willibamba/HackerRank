#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr with the missing numbers
#  2. INTEGER_ARRAY brr of the original numbers
#

def missingNumbers(arr, brr):
    # Write your code here
    # Loop over arr, check if each number is present in brr once and remove it
    # Return the remaining numbers in brr as sorted list of distinct value(s)
    
    for number in arr:
        for present in brr:
            
            if number == present:
                brr.remove(present)
                break
            
    return sorted(list(set(brr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()