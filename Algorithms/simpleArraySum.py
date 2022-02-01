#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum():
    # Write your code here
    num = input()
    numlist = [int(numlist) for numlist in input().split(" ")]
    print(sum(numlist))


if __name__ == '__main__':
    simpleArraySum()
