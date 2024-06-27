import numpy as np
from numpy import load

data = load(file="cost.npz")
print("key from file", data)
# key from file NpzFile 'cost.npz' with keys: array
print("Data from file", data['array'])
