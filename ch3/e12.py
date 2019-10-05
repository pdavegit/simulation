import random
import math
from collections import defaultdict

def fn():
    sum = 0
    n = 0
    while sum < 1:
        r = random.random()
        sum = sum + r
        n += 1
    return n

def e(iterations):
    sum_n = 0
    for i in range(iterations):
       n = fn()
       sum_n += n
    return (sum_n/iterations)

print(100, e(100))
print(1000, e(1000))
print(10000, e(10000))
print(100000, e(100000))
