#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps = numSwaps + 1

    
print(f"Array is sorted in {numSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[len(a) - 1]}")
 
