#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference():
    # Write your code here
    matrix = []

    num = int(input())
    for i in range(num):
        lis = [int(numlist) for numlist in input().split(" ")]
        matrix.append(lis)
    bb = 0
    for i in range(len(matrix)):
        bb += matrix[i][i]
        pass
    a = 0
    b = len(matrix[0]) - 1
    aa = 0
    for j in range(len(matrix)):
        aa += matrix[a][b]
        a += 1
        b -= 1

    return abs(aa-bb)


if __name__ == '__main__':
    print(diagonalDifference())
