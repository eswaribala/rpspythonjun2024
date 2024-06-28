'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hi', 'Welcome', 'to', 'Python training')


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='RPS', mid='Consulting', last='Python')

from time import sleep
from datetime import datetime
 
class Sleeper:
    def __init__(self, secs1,sec2):
        self.__secs = secs1
 
    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            print(*args,**kwargs)
            sleep(self.__secs)
            return fn(*args, **kwargs)
 
        return wrapped
 
 
@Sleeper(10,20)
def send_message(name):
    print("Hi {}, it is now: {}".format(name, datetime.now()))
 
for x in range(5):
    send_message("Important")
    
    
    
    
    
    
    