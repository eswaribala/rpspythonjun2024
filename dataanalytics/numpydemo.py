import random

import numpy
import numpy as np

# generate random number within the boundary of 100 and 5 by 5 matrix
cost = np.random.randint(100, size=(5, 5))
print(cost)
print("Shape of the array", cost.shape)
print("Size of the array", cost.size)
print("Type of the array", type(cost))
print("Type of the array elements", cost.dtype)
# reduce the cost
print("10% reduction in cost", cost - 0.01)
# sale price

print("20% margin as sale price", cost + 0.20)

# array transpose
customer_data = np.random.randint(100000, size=(3, 4))
print("Customer Data\n", customer_data)
print("Transposed Customer Data\n", customer_data.T)

# loans
housing_loans = np.random.randint(100000000, size=(2, 2))
car_loans = np.random.randint(100000000, size=(2, 2))
cc_loans = np.random.randint(100000000, size=(2, 2))
print("Housing Loans\n", housing_loans)
print("Car Loans\n", car_loans)
print("CC Loans\n", cc_loans)
# accumulating all the loans
print("Accumulated Loans\n", np.add(housing_loans, car_loans, cc_loans))

# nd array to list
print("Accumulated Loans List\n", list(np.add(housing_loans, car_loans, cc_loans)))

# convert list to array
salary = []
for i in range(1, 100):
    salary.append(random.randint(1, 100000))
print("Generated Salary\n", salary)

# convert list to array and remove duplicates
print("Array of Generated Salary\n", numpy.asarray(salary))

# generate data and index
data = np.arange(20, 0, -2)
print(data)
# fetch data by index
# it picks data from index position
new_data = data[np.array([0, 4, 6, 2])]
print("Indexed Data\n", new_data)

# data slicing
print("Slice the data from array\n", data[2:8])

scores = np.random.randint(100, size=(6, 5))
print("Scores of the trainees\n", scores)
# sorted data
print("Scores of the trainees\n", np.sort(scores, axis=1, kind='quicksort'))


# conditional data
selected_scores= np.where(scores > 75)
print("Get Selected Score\n", scores[selected_scores])
