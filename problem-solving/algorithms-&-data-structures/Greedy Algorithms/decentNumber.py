#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#
# Sample Input: n = 1, n = 3, n = 5, n = 11
#
# Sapmle Output: -1, 555, 33333, 55555533333
#

def decentNumber(n):
    # Write your code here
    # Hence they result to 1 digit, which is Undecent number 
    if n in [1,2,4,7]:
        print("-1")
        return
    
    # The main logic for finding the largest Decent number divisible by 3 and/or 5,
    # The number of 3's it contains is divisible by 5
    # The number of 5's it contains is divisible by 3
    threes = 0
    while n % 3 != 0:
        n -= 5
        threes += 5
        
    print("5" * n, "3" * threes, sep="")
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)