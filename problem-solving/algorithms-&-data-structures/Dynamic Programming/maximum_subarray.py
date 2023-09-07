#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Sample Input: arr = [2, -1, 2, 3, 4, -5]
#
# Sample Output: maximum subarray = [2, -1, 2, 3, 4] = 10
#                maximum subsequence = [2, 2, 3, 4] = 11
#                return [10, 11]

def maxSubarray(arr):
    # Write your code here
    # Set the subarray, maximum subarray and maximum subsequence
    sub_arr = 0
    max_sub = max(arr)
    max_seq = 0
    for i in range(len(arr)):
        # Add subarray value to the arr value and if greater than arr value
        # assing it as subarray value
        sub_arr = max(arr[i], sub_arr + arr[i])
        
        # If true, assign subarray value as maximum subarray value  
        if sub_arr > max_sub:
            max_sub = sub_arr
            
        # If arr value is greater than 0, increment maximum subsequence with arr value 
        if arr[i] > 0:
            max_seq += arr[i]
    
    if max_sub <= 0:
        return [max_sub, max_sub]
    
    return [max_sub, max_seq]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
