#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(startPoint, endPoint, appleTree, orangeTree, apples_distances, oranges_distances):
    # Write your code here
    fallenApples = 0
    fallenOranges = 0
    for i in range(len(apples_distances)):
        if apples_distances[i] + appleTree in range(startPoint, endPoint+1):
            fallenApples += 1
    for i in range(len(oranges_distances)):
        if oranges_distances[i] + orangeTree in range(startPoint, endPoint+1):
            fallenOranges += 1
    print(fallenApples)
    print(fallenOranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
