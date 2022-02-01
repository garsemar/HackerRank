#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    base = 1
    space = n-base
    for i in range(n):
        if base > n:
            break
        for j in range(space):
            print(" ", end="")
        space -= 1
        for x in range(base):
            print("#", end="")
        print("")
        base += 1


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
