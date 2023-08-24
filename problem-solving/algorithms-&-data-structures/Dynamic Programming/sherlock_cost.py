#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#
# Sample Input: B = [10, 1, 10, 1, 10]
#
# Sample Output: |1-10| + |10-1| + |1-10| + |10-1| = 36
#

def cost(B):
    # Write your code here
    # Assign minimum and maximum sum with 0
    min_sum = 0
    max_sum = 0
    # The main logic to calculate maximum sum
    for i in range(1, len(B)):
        
        temp = max(min_sum, max_sum + abs(B[i-1] - 1))
        max_sum = max(min_sum + abs(1 - B[i]), max_sum + abs(B[i] - B[i-1]))
        min_sum = temp
        
    return max(min_sum, max_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
