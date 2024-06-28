from multiprocessing import Pool
import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())




import numpy as np
from time import time
print(np.random.randint(5, size=(2, 4))) #within 5 , 2x4 samples
# Prepare data
#constructs a random number generator.
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
#print(data)








def compute(x):
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    # Define the dataset
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    # Output the dataset
    print ('Dataset: ' + str(dataset))

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 5
    chunksize = 3
    with Pool(processes=agents) as pool:
        result = pool.map(compute, dataset, chunksize)

    # Output the result
    print ('Result:  ' + str(result))






