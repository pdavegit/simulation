import math
import random

def g(x, y):
    return math.exp((x+y)**2)

def e8(iterations):
    s = 0
    for i in range(iterations):
        r1 = random.random()
        r2 = random.random()
        s = s + g(r1, r2)
    return s/iterations

# Value from WolframAlpha is 4.89916

print(e8(1000000))
