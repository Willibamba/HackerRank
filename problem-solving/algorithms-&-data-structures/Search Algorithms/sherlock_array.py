#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # Declare and assign left side with 0 and right side with sum of all the values in the array
    leftSum, rightSum = 0, sum(arr)
    
    # Iterate through the array
    # Decrement the right side by the current value
    # Compare if the left and right side are equal, return YES
    # Else, increment the left side with the current value
    for i in range(len(arr)):
        
        rightSum -= arr[i]
        
        if leftSum == rightSum:
            return "YES"
        
        leftSum += arr[i]
        
    # If the left and right side are not equal, return NO   
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
