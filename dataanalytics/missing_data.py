# Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
print(dataset.shape)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values  # dataset.iloc[:,3:]
print(y)
print(X)
# Taking care of missing data
# from sklearn.preprocessing import SimpleImputer
# Imputer()
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
# imputer = imputer.fit(X[:, 1:3])
# print(imputer)
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])
print(X[:, 2])
print(X[:, 1])

dataset = pd.read_csv("F:/citi_ml_jun2018/day3/LinearRegression/black-friday/BlackFriday.csv")
# print(dataset.iloc[:,9])
X = dataset.iloc[:, :].values
from sklearn.impute import SimpleImputer

# Imputer()
imputer = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0)
X[:, 10:11] = imputer.fit_transform(X[:, 10:11])
'''
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',100)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.width',None)
'''

print(X[0:5, 9])

print(X[0:10, 10])
