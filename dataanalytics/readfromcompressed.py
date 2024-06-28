# load numpy array from npz file
from numpy import load
# load dict of arrays
dict_data = load('data_2.npz')
# extract the first array
data = dict_data['arr_0']
# print the array
print(data)