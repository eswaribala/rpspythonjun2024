from numpy import asarray
from numpy import savez_compressed
# define data
data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
# save to npy file
savez_compressed('data_2.npz', data)