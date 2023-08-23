#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Sample Input: arr = [10, 7, 12]
#
# Sample Output: Add 5 -> [15, 12, 12], Add 2 -> [15, 14, 14], Add 1 -> [15, 15, 15] 
#               Return 3
#              

def equal(arr):
    # Write your code here
    # Assign minimum number of operations (op1, op2, op3) to 0 and m as minimum value in arr array
    op1, op2, op3, = 0, 0, 0
    m = min(arr)
    
    # Iterate through the arr array, calculate the difference of m from each value
    # Calculate the number of pieces (1, 2 or 5) to give each from the difference,
    # difference plus 1, difference plus 2 and increment operations respectively
    for val in arr:
        diff = (val - m)
         
        op1 += int(diff/5) + int(diff%5/2) + int(diff%5%2)
        op2 += int((diff+1)/5) + int((diff+1)%5/2) + int((diff+1)%5%2)
        op3 += int((diff+2)/5) + int((diff+2)%5/2) + int((diff+2)%5%2)
        
    # Return the minimum number of operations
    return min(op3, min(op2, op1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()