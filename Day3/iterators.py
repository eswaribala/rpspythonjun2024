# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:19:01 2018

@author: Balasubramaniam
"""

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
#next(my_iter)


# create an iterator object from that iterable
iter_obj = iter(my_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            
for i in PowTwo(5):
    print(i)
    

#generator
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

val = countdown(5)
for x in val:
    print(x)  
#generator
print("Generators.......")
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
        yield 3 ** n

        
for i in PowTwoGen(5):
    print(i)
    
