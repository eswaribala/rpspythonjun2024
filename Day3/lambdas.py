'''
 -*- coding: utfs-8 -*-
'''
"""
Created on Sun Dec 23 19:37:50 2018

@author: Balasubramaniam
"""
#no arguments
f = lambda: True
f()
#single argument
data = lambda x:x%2
print(data(5))

#multiple arguments
r = lambda x, y: x * y
print(r(12, 3))   # call the lambda function
'''
Map is a Python built-in function that takes in a function and 
a sequence as arguments and then calls the input 
function on each item of the sequence.
'''
import math
dataList=[89,35,78,90,45,27,78,22]

odd_list = map(lambda x: math.log2(x), dataList)
for _ in odd_list:
    print(_)


orders=[["34587", "Learning Python, Mark Lutz", 
         400, 40.95],
        ["34545", "Mastering Python, Mark Lutz", 
         3, 90.95]
        ]
min_order=100
invoice_total=map(lambda x:x if x[2] >= min_order 
                       else ( x[3] + 10),orders)
for _ in invoice_total:
    print(_)


#filter vs map
list_a = [1, 2, 3]
list_b = [10, 20, 30]
def even_fn(x):
  if x % 2 == 0:
    return True
  return False

#result = filter(even_fn, list_a, list_b)
result1 = filter(even_fn, list_a)
print("result1")
for _ in result1:
    print(_)

print("result2")
result2 = map(even_fn, list_a)
for _ in result2:
    print(_)


result3 = map(lambda x, y: x + y, list_a, list_b)
for _ in result3:
    print(_)
from functools import reduce

#reduce
rlist = [1,2,3,4,5]
s = reduce(lambda x,y: x+y,  rlist)
print(s)


weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs' 'fri']
days = filter(lambda day: day if len(day)==3 else '', weekdays)
for d in days:
   print(d)

numbers = [ 74, 85, 14, 23, 56, 31,44 ]

remainders = map(lambda num: num%5, numbers)
for i in remainders:
   print(i)

colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]



def normalize_case(string):
    return string.casefold()

normalized_colors = map(normalize_case, colors)

for i in normalized_colors:
   print(i)


#object sorting

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
print([item.name for item in L])

L = [lambda x: x ** 2,
         lambda x: x ** 3,
         lambda x: x ** 4]

for f in L:
	print(f(3))
    
key = 'quadratic'
print({'square': (lambda x: x ** 2),
     'cubic': (lambda x: x ** 3),
     'quadratic': (lambda x: x ** 4)}[key](10))    
    


    
    
    
    
    
    
