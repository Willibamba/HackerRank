#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#
# Sample Input: n = 16
#
# Sample Output: n[0] = 1, n[1] = 6
#                (1 * 10) + (2 * 6) % 1000000007 = 22 -> 22 + 1 % 1000000007 = 23
#                

def substrings(n):
    # Write your code here
    mod = ((10**9) + 7)
    total = fdn = int(n[0])
    
    # The logic to compute the sum of the integer values of all substrings in n,
    # Return n modulo 10**9 + 7
    for i in range(1, len(n)):
        
        fdn = (fdn * 10) + ((i+1) * int(n[i])) 
        
        total = (total + fdn) 
        
    return total % mod
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
