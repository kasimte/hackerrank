"""
HackerRank
Interview Preparation Kit
Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    altitude = 0
    
    for char in s:
        if char == "U":
            altitude = altitude + 1
        else:
            altitude = altitude - 1

        if altitude == 0 and char == "U":
            valleyCount = valleyCount + 1

    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
