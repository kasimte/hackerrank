#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # c is something like [0,1,0,0,0,1,0]
    # filter to safe path
    safe = []
    for index, value in enumerate(c):
        if value == 0:
            safe.append(index)

    # filter to shortest safe path
    shortest = []

    for i, v in enumerate(safe):
        # v is not part of shortest path if
        before = v - 1
        after = v + 1

        # v - 1 is already part of the shortest path
        # v + 1 is a safe index
        if before in shortest and after in safe:
            next
        else:
            shortest.append(v)

    # return the number of steps in shortest
    return len(shortest) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
