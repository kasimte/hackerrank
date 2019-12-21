#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    i = 1
    while i < 11:
        print(f'{n} x {i} = {n * i}')
        i = i + 1
