#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    # Write your code here
    # A train_data dictionary to hold the train tracks and tracks for the maximum cell nummber
    train_data = {}
    tracks = n * m
    
    if k == 0:
        return tracks
    
    ''' Loop over the train tracks to check if the track index is in train data
    as train track may overlap other train tracks in the row,
    If true, check if the start point ie lesser and/or end is greater than the current track,
    If yes, assign current track as start and/or end,
    Else, add the current track starting and ending points with the train track index to the train_data dictionary'''  
        
    for train in track:
        print(train)
        
        if train[0] in train_data.keys():
            start = train_data[train[0]][0]
            end = train_data[train[0]][1]
            if start > train[1]:
                train_data[train[0]][0] = train[1]
            if end < train[2]:
                train_data[train[0]][1] = train[2]
        else:
            train_data[train[0]] = train[1:]
            
    print(train_data)
    
    #Loop over for each train index in train_data, 
    # Subtract the starting point from the end point and add one to remainder, 
    # Then decrement the total track cells by the remainder''' 
    for train in train_data.values():
        tracks -= ((train[1]-train[0]) + 1)
       
    return tracks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
