'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''


str = "formidable"

for e in str:
   print(e, end=" ")

print()

it = iter(str)

print(it.__next__())
print(it.__next__())
print(it.__next__())

print(list(it))


class Seq:
    def __init__(self):
        self.x = 0

    def __next__(self):
        self.x += 1
        return self.x ** self.x

    def __iter__(self):
        return self


s = Seq()
n = 0

for e in s:

    print(e)
    n += 1

    if n > 10:
        break

class ReadData(object):
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def __iter__(self):
        return(self)
    def __next__(self):
        if(self.min>self.max):
            raise StopIteration('Exceeded the limit')
        else:
            self.min+=5
            return self.min-5
        
readData=ReadData(50,100)
print(next(readData))

iterableData = iter(readData)
while True:
    try:
       print(iterableData.__next__(),end='') 
    except StopIteration as e:
       print() 
       print(e) 
       break
           

            
         