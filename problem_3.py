#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = []
    bob = []
    total = []
    for i in a:
        for j in b:
            if i > j:
                alice = alice + [1]
            elif i > j:
                bob = bob + [1]
            elif i == j:
                alice = alice + [0]
                bob = bob + [0]
    total = sum(alice) + sum(bob)
    return total
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()