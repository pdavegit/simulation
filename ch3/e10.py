import numpy as np

# Using Numeric Python

u = np.random.rand(100000)
expu = np.exp(u)
print(np.cov(u, expu))
# Answer 0.14

