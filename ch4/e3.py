import math
import random

def g(x):
    return math.exp(math.exp(x))

def h(a, b, y):
    return (b-a)*g(a + (b-a)*y)

def e3(iterations):
    a = 0
    b = 1
    s = 0
    for i in range(iterations):
        r = random.random()
        s = s + h(a, b, r)
    return s/iterations

# Value from WolframAlpha is 6.31656

print(e3(1000000))
