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

def downToZero(n):
    # Write your code here
    temp = set()
    count = 0
    N = deque([[n, count]])
    
    while N:
        n, count = N.popleft()
        
        if n <= 1:
            if n == 1:
                count += 1
            break
        if n-1 not in temp:
            temp.add(n)
            N.append([n-1, count+1])
            print(n-1)
        for i in range(int(math.sqrt(n)), 1, -1):
           
            if n % i == 0:
                factor = max(i, n/i)
                if factor not in temp:
                    temp.add(factor)
                    N.append([factor, count+1])
                    
    print(temp)
    return count
       
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
