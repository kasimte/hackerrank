#!/bin/python3

# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

import sys

S = input().strip()

def num(s):
    try:
        return int(s)
    except:
        return "Bad String"

convert = num(S)
print(convert)
