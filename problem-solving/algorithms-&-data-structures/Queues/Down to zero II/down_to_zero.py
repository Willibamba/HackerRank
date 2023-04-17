#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
precompute = [0, 1, 2, 3] 
def downToZero(n):
    # Write your code here
    count = 0
    while n >= len(precompute):
        l = len(precompute)
        
        mini = precompute[l-1]
        
        for i in range(int((math.sqrt(l))), 1, -1):
            if l % i == 0:
            
                li = int(l/i)
                mini = min(mini, precompute[li])
                
                
        precompute.insert(l, 1+mini)
        
    
    return precompute[n]
       
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
