#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#
# Sample Input: k = 10, A = [2, 1, 3], B = [7, 8, 9]
#
# Sample Output: Sorted A = [1, 2, 3], B = [9, 8, 7],
#                A[0] + B[0] = 1 + 9 = 10 >= k
#                A[1] + B[1] = 2 + 8 = 10 >= k
#                A[2] + B[2] = 3 + 7 = 10 >= k
#                return YES

def twoArrays(k, A, B):
    # Write your code here
    # Sort array A in ascending order and array B in descending order
    A.sort()
    B.sort(reverse=True)

    # Loop for index in A and it's corresponding index in B and sum the values,
    # if any of the sum is less than k return NO, if none return YES
    for i in range(len(A)):

        if A[i] + B[i] < k:
            return "NO" 
              
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
