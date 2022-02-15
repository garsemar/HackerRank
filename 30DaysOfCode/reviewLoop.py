#!/bin/python3

import math
import os
import random
import re
import sys


def string(n):
    listP = []
    listI = []
    for i in range(len(n)):
        if i % 2 == 0:
            listP.append(n[i])
        elif i % 2 != 0:
            listI.append(n[i])
    for j in listP:
        print(j, end="")
    print(" ", end="")
    for x in listI:
        print(x, end="")
    print("")


if __name__ == '__main__':
    i = int(input().strip())
    while i != 0:
        n = input().strip()
        string(n)
        i -= 1
