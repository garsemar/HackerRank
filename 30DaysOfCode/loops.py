#!/bin/python3

import math
import os
import random
import re
import sys


def mult(n):
    for i in range(10):
        print(f"{n} x {i+1} = {n*(i+1)}")


if __name__ == '__main__':
    n = int(input().strip())
    mult(n)
