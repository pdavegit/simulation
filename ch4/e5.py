import math
import random

def g(x):
    return math.exp(x + x*x)

def h(a, b, y):
    return (b-a)*g(a + (b-a)*y)

def e5(iterations):
    a = -2
    b = 2
    s = 0
    for i in range(iterations):
        r = random.random()
        s = s + h(a, b, r)
    return (s/iterations)

# Value from WolframAlpha is 93.1628

print(e5(1000000))
