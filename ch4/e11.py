import numpy as np

# Using Numeric Python
u = np.random.rand(10000000)
print(np.corrcoef(u, np.sqrt(1-u*u)))
# Answer -0.9214
print(np.corrcoef(u*u, np.sqrt(1-u*u)))
# -0.98
