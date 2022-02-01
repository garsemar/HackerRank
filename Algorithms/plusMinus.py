#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] == abs(arr[i]) and arr[i] != 0:
            pos += 1
        elif arr[i] != abs(arr[i]):
            neg += 1
        else:
            zero += 1
    pos = "{:.6f}".format(pos/n)
    neg = "{:.6f}".format(neg/n)
    zero = "{:.6f}".format(zero/n)
    print(pos)
    print(neg)
    print(zero)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr, n)
