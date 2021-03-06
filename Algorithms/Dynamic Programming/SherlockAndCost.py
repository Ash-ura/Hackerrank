#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    hi, low = 0, 0
    for i in range(1, len(B)):
        high_to_low_diff = abs(B[i-1] - 1)
        low_to_high_diff = abs(B[i] - 1)
        high_to_high_diff = abs(B[i] - B[i-1])
        
        low_next = max(low, hi+high_to_low_diff)
        hi_next = max(hi+high_to_high_diff, low+low_to_high_diff)
        
        low = low_next
        hi = hi_next
    
    return max (hi,low)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
