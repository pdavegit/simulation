import math
import random

def indicator(x1, x2):
    if x1 > x2:
        return 0
    else:
        return 1

def g(x1, x2):
    return math.exp(-(x1 + x2))*indicator(x1, x2)

def h(y1, y2):
    return g(1.0/y1 - 1, 1.0/y2 - 1)/((y1*y1)*(y2*y2))

def e9(iterations):
    s = 0
    for i in range(iterations):
        u1 = random.random()
        u2 = random.random()
        s = s + h(u1, u2)
    return s/iterations

# Wolfram 0.5

print(e9(100000))

