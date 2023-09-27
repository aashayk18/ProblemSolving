import math 
import os 
import random 
import re 
import sys

def plusMinus(arr):
    print(*[round(sum(1 for i in arr if i > 0) / len(arr), 6)])
    print(*[round(sum(1 for i in arr if i < 0) / len(arr), 6)])
    print(*[round(sum(1 for i in arr if i == 0) / len(arr), 6)])


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)