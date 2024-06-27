import numpy as np
from numpy import savez_compressed
cost = np.random.randint(100, size=(5, 5))
print(cost)
savez_compressed(file="cost.npz",array=cost)