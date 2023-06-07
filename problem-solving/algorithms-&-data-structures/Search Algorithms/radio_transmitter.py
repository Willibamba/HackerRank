#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    # Sort the x array, assign transmission range and distances and antennae
    x.sort()
    tansmitter_range = k 
    transmitter_coverage = 0
    antennae = 0
      
    for house in range(len(x)-1):
        # Check if current house is within the distance of transmission area
        if x[house] <= transmitter_coverage:
            continue
        
        else:
            # If next house and current house are within transmission range
            # If true, subtract the distances and assign as transmission range
            new_range = x[house] + tansmitter_range
            if x[house+1] <= new_range:
                tansmitter_range = new_range - x[house+1]
                
            else:
                # Increment transmitter by 1, assign transmitter range to k 
                # And install new transmitter on the current house
                antennae += 1
                tansmitter_range = k
                transmitter_coverage = x[house] + k
    
    # If the distance of nth house beyond the tansmission range, increment antennae by 1 
    if x[-1] > transmitter_coverage:
        antennae += 1
            
    return antennae

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()