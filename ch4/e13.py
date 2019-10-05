import random
import math
from collections import defaultdict

def fn():
    prod = 1
    n = 0
    while prod >= math.exp(-3):
        r = random.random()
        prod = prod * r
        n += 1
    return n - 1


sum_n = 0
iterations = 1000000
freq = defaultdict(int)
for i in range(iterations):
    n = fn()
    sum_n += n
    freq[n] += 1

print(sum_n/iterations)
for i in range(7):
    print(i, freq[i]/iterations)
