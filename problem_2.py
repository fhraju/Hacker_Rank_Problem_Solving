#!/bin/python

import math
import os
import random
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for i in ar[0:]:
        sum = sum+i
    return sum

print(simpleArraySum(ar = list(input())))
