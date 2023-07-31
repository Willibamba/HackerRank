#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
# Sample Input: k = 3, contests = [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
#
# Sample Output: 5 + 2 + 8 + 10 + 5 - 1 = 29

def luckBalance(k, contests):
    # Write your code here
    important = []
    unimportant = []
    
    ''' Iterate through the contests array, if rate is 1, add luck amount in important array or 
        rate is 0, add luck amount in unimportant array ''' 
    for contest in contests:
        if contest[1] == 1:
            important.append(contest[0])
        elif contest[1] == 0:
            unimportant.append(contest[0])
            
    # Sort important array in descending order and assign sum of unimpotant array to maximum luck        
    important.sort(reverse=True)
    max_luck = sum(unimportant)
    
    # Calculate the maximum luck
    for i in range(len(important)):
        if i >= k:
           max_luck -= important[i]
        elif i <= k-1:
            max_luck += important[i] 
             
    return max_luck
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()