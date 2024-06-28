# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:09:33 2020

@author: Balasubramaniam
"""

from pandas import DataFrame

Cars = {'Brand': ['Honda Civic','Ford Focus','Toyota Corolla','Toyota Corolla','Audi A4'],
        'Price': [22000,27000,25000,29000,35000],
         'Year': [2014,2015,2016,2017,2018]
        }

df = DataFrame(Cars, columns= ['Brand', 'Price','Year'])

count1 = df['Price'].count()
print('count: ' + str(count1))

mean1 = df['Price'].mean()
print('mean: ' + str(mean1))

std1 = df['Price'].std()
print('std: ' + str(std1))

min1 = df['Price'].min()
print('min: ' + str(min1))

quantile1 = df['Price'].quantile(q=0.25)
print('25%: ' + str(quantile1))

quantile2 = df['Price'].quantile(q=0.50)
print('50%: ' + str(quantile2))

quantile3 = df['Price'].quantile(q=0.75)
print('75%: ' + str(quantile3))

max1 = df['Price'].max()
print('max: ' + str(max1))

# importing pandas module
#merging
import pandas as pd
# Define a dictionary containing employee data
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32], }

# Define a dictionary containing employee data
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2)

print(df, "\n\n", df1)

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32]}

# Define a dictionary containing employee data
data2 = {'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=['K0', 'K1', 'K2', 'K3'])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])

print(df, "\n\n", df1)
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","PySpark","Spark"],
    'Fee' :[20000,25000,26000,22000,24000,3000],
    'Duration':['30day','40days','35days','40days','60days','60days'],
    'Discount':[1000,2300,1200,2500,2000,2000]
              }
df = pd.DataFrame(technologies)
print(df)

# Using Aggregate Functions on DataFrame
result = df[['Fee','Discount']].aggregate('sum')
print(result)

# Use DataFrame.group() Function
#result = df.groupby('Courses')['Fee','Discount'].aggregate('sum')
#print(result)

# Using Aggregate Function on Series
value = df['Fee'].aggregate('sum')
print(value)

# Using groupby() and aggreaget()
result = df.groupby('Courses').aggregate('sum')
print(result)

# Using groupby() and aggreaget()
#result = df.groupby('Courses')['Fee','Duration'].aggregate('sum')
#print(result)

# Alternate way
result = df[['Courses','Fee','Duration']].groupby('Courses').aggregate('sum')
print(result)

# Directly using sum() function
result = df.groupby('Courses').sum()
print(result)

# Groupby & multiple aggregations
result = df.groupby('Courses')['Fee'].aggregate(['min','max'])
print(result)

# Groupby multiple columns & multiple aggregations
result = df.groupby('Courses').aggregate({'Duration':'count','Fee':['min','max']})
print(result)