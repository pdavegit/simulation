import math
import random

def g(x):
    return (1-x*x)**(3.0/2.0)

def h(a, b, y):
    return (b-a)*g(a + (b-a)*y)

def e4(iterations):
    a = 0
    b = 1
    s = 0
    for i in range(iterations):
        r = random.random()
        s = s + h(a, b, r)
    return (s/iterations)

# Value from WolframAlpha is 0.589049

print(e4(1000000))
