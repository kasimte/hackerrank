#!/bin/python3

# https://www.hackerrank.com/challenges/30-2d-arrays/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # 1) identify all of the hourglasses
    # identify an hourglass by its upper left coordinate [x,y]
    coordinates = [[i,j] for i in range(4) for j in range(4)]

    # 2) find a way to sum a particular hourglass
    def sumHourglass(arr, coord):
        x = coord[0]
        y = coord[1]
        aSum = 0
        for i in range(3):
            for j in range(3):
                aSum += arr[i+x][j+y]
        aSum -= arr[x+1][y]
        aSum -= arr[x+1][y+2]
        return aSum

    # 3) track and output the maximum
    sums = []
    for c in coordinates:
        sums.append(sumHourglass(arr, c))
    print(max(sums))
