#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#
# Sample Input: calorie = [5,10,7]
#
# Sample Output: (2^0 x 10) + (2^1 x 7) + (2^2 x 5) = 10 + 14 + 20 = 44
#
#

def marcsCakewalk(calorie):
    # Write your code here
    # Sort the calorie array in descending order and assign miles with 0
    calorie.sort(reverse=True)
    miles = 0
    
    # Iterate through the sorted calorie array and calculate the minimum miles
    for i in range(len(calorie)):
        
        miles += (2 ** i) * calorie[i]
           
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()