'''
Created on 23-Nov-2017

@author: BALASUBRAMANIAM
'''
from time import sleep
from datetime import datetime
 
def timed(fn):
    def wrapped():
        print("Current time: {}".format(datetime.now()))
        return fn()
    return wrapped

 
@timed #annotation
def message():
    print("Greeting!")
 
 
for x in range(5):
    message()
    sleep(10)
    
    
    
    
    
    
    
    
    
    
    