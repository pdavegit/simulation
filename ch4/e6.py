import math
import random

def g(x):
    return x * (1 + x*x)**-2

def h(y):
    return g(1.0/y-1.0)/(y*y)

def e6(iterations):
    s = 0
    for i in range(iterations):
        r = random.random()
        s = s + h(r)
    return s/iterations

# Value from WolframAlpha is 0.5

print(e6(1000000))
