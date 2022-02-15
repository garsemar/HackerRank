#!/bin/python3

import math
import os
import random
import re
import sys


def reverse(ar):
    ar = list(reversed(ar))
    for i in ar:
        print(i, end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse(arr)
