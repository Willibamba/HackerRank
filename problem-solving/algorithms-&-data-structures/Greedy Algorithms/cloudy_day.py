#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#
# Sample Input: p = [10,100], x = [5,100], y = [4], r = [1]
#
# Sample Output: cloudy town = begin = 4-1 = 3, end = 4+1 = 5 -> x[0] -> p[0] = 10
#                sunny town = 100
#                return 10 + 100 = 110
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    # Create cities array, iterate and add the beginning and ending of the clouds 
    # And location of the towns
    cities = []
    for i in range(len(y)):
        begin = y[i] - r[i]
        end = y[i] + r[i] 
        cities.append( (begin,0,i) )
        cities.append( (end,2,i) )
        
    for i in range(len(x)):
        cities.append( (x[i],1,i) ) 
    
    # traverse the sorted clouds array by updating the people in sunny town and cloudy town
    sunny_town = 0
    cloud = set()
    cloudy_town = defaultdict(int)
    for (pos,num,i) in sorted(cities):
        if num == 0:
            cloud.add(i)
        elif num == 1:
            if len(cloud) == 0:
                sunny_town += p[i]
            elif len(cloud) == 1:
                cloudy_town[list(cloud)[0]] += p[i]
        elif num == 2:
            cloud.remove(i)
    
    # If there is cloudy town(s) return the maximum cloudy town with people plus sunny town else return sunny town
    if len(cloudy_town) == 0:
        return sunny_town + max(cloudy_town.values())
       
    return sunny_town 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
