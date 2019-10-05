import math
import random

def g(x):
    return math.exp(-x*x)

def h(y):
    return g(1.0/y-1.0)/(y*y)

def e7(iterations):
    s = 0
    for i in range(iterations):
        r = random.random()
        s = s + h(r)
    return s/iterations

# Value from WolframAlpha is 1.77245
# The function g is symmetric therefore Integral[-inf, inf] = 2 * Integral[0, inf]
print(2.0*e7(1000000))
