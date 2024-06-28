'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''


def gen():
    x, y = 1, 2
    yield x, y

    x += 1
    yield x, y


g = gen()

print(next(g))
print(next(g))

try:
    print(next(g))

except StopIteration:
    print("Iteration finished")

import random 
def gen7digitnumber():
    #gen six numbers between 1 to 40
    for i in range(6):
        yield random.randint(1,40)
        
    #gen 7th digit in the range of 1 to 15
    
    #yield random.randint(1,15)
    
    
for i in range(10):
    for number in gen7digitnumber():
        print(number,end='')
    print()