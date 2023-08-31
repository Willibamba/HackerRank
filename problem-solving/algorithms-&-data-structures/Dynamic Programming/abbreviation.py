#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
# Sample Input: a = AbcDE, b = ABDE
#
# Sample Output: In string a, we can convert "b" and delete "c" to match string b
#                So we return "YES"

def abbreviation(a, b):
    # Write your code here
    # Create a 2-D dp array of False values with sizes a and b and increment by 1
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    
    # Turn the first indexes to True
    dp[0][0] = 1
    
    # Iterate through a and b array, check the conditions and/or update the dp array
    for i in range(len(a)):
        for j in range(len(b)+1):
            if dp[i][j]:
                if j < len(b) and a[i].upper() == b[j]:
                    dp[i+1][j+1] = 1
                    
                if a[i].islower():
                    dp[i+1][j] = 1
                     
    
    # If the lengths of the 2-D dp array are equal, return "YES" else return "NO" 
    if dp[len(a)][len(b)]:
        return "YES"
    return "NO"
    
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()