import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print("An array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype='complex')
print("An array initialized with all 6s."
      "Array type is complex:\n", d)

# basic operations
# Create an array with random values
e = np.random.random((2, 2))
print("A random array:\n", e)

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:", a + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)

# square each element
print("Squaring each element:", a ** 2)

# modify existing array
a *= 2
print("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate"
      "columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),"
      "(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print("\nElements greater than 0:\n", temp)

# Python program to demonstrate
# unary operators in numpy

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis = 1))

# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))

# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())

# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))

# Python program to demonstrate
# binary operators in Numpy

a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])

# add arrays
print ("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)

# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))

# Python program to demonstrate
# universal functions in numpy

# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.sqrt(a))

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

# sorted array
print("Array elements in sorted order:\n",
      np.sort(a, axis=None))

# sort array row-wise
print("Row-wise sorted array:\n",
      np.sort(a, axis=1))

# specify sort algorithm
print("Column wise sort by applying merge-sort:\n",
      np.sort(a, axis=0, kind='mergesort'))

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n",
      np.sort(arr, order=['grad_year', 'cgpa']))

#conditional
import numpy as np

# a is an array of integers.
a = np.array([[1, 2, 3], [4, 5, 6]])

print(a)

print('Indices of elements <4')

b = np.where(a < 4)
print(b)

print("Elements which are <4")
print(a[b])

#structured

a = np.array([('Sana', 2, 21.0), ('Mansi', 7, 29.0)],
             dtype=[('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float64)])

# Sorting according to the name
b = np.sort(a, order='name')
print('Sorting according to the name', b)

# Sorting according to the age
b = np.sort(a, order='age')
print('\nSorting according to the age', b)

#reshape
# Python Program illustrating
# numpy.reshape() method

# array = geek.arrange(8)
# The 'numpy' module has no attribute 'arrange'
array1 = np.arange(8)
print("Original array : \n", array1)

# shape array with 2 rows and 4 columns
array2 = np.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n",
      array2)

# shape array with 4 rows and 2 columns
array3 = np.arange(8).reshape(4, 2)
print("\narray reshaped with 4 rows and 2 columns : \n",
      array3)

# Constructs 3D array
array4 = np.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n",
      array4)

# make a matrix with numpy
gfg = np.matrix('[1, 2; 4, 5; 7, 8]')

# applying matrix.reshape() method
reshaped_matrix = gfg.reshape((2, 3))

print(reshaped_matrix)