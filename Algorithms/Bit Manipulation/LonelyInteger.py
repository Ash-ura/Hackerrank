#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    result = a[0]
    for i in range(1, len(a)):
        result ^= a[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    
    fptr.write(str(result) + '\n')

    fptr.close()
