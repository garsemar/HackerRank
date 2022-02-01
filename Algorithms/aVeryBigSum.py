#!/bin/python3
def aVeryBigSum():
    # Write your code here
    num = input()
    numlist = [int(numlist) for numlist in input().split(" ")]
    print(sum(numlist))


if __name__ == '__main__':
    aVeryBigSum()
