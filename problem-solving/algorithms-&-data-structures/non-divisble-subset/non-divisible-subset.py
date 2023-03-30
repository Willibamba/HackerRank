#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    S = [0] * k
    for i in s:
        remainder = i % k
        S[remainder] += 1
    count = 0 
    for j in range(1, math.ceil(k / 2)):
        count += max(S[j], S[-j])
    if S[0]:
        count += 1
    if k % 2 == 0:
        if S[int(k/2)]:
            count += 1
    
    
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
