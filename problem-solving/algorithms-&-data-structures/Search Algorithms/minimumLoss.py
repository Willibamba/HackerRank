#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
# Example Input: price = [20, 15, 8, 2, 12]
# Example Output: Minimum loss is purchasing at price[1] = 15 and reselling at    price[4] = 12. Return 15 - 12 = 3
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    # Map the prices, store each value and index as year key and value pairs
    year = {}
    for i, val in enumerate(price):
        year[val] =  i 
        
    # Sort the prices in descending order and set minimal loss to the highest value
    prices = sorted(price, reverse=True)
    minimal = prices[0]
    
    # Loop over the prices, compare price years(indexes) and the differences for minimal loss
    for j in range(len(prices)-1):
        
        loss = prices[j] - prices[j+1]
        print(loss)
        if loss < minimal and year[prices[j]] < year[prices[j+1]]:
            minimal = loss
         
    return minimal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
