#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# Sample Input: n = 6, arr = [4,6,4,5,6,2]
#
# Sample Output: sum of students = [1,2,1,2,3,1] = 10
#                

def candies(n, arr):
    # Write your code here
    # Set all indexes in students array with a value of 1 
    students = [1] * n
    
    # Traverse from left to right and update the students array
    for i in range(1, n):
        
        if arr[i-1] < arr[i]:
            students[i] = students[i-1]+1
    
    # Traverse from right to left and update the students array
    for i in range(n-2, -1, -1):
        
        if arr[i] > arr[i+1]:
            students[i] = max(students[i], students[i+1] + 1)
    
    return sum(students)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
