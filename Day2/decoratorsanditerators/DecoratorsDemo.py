'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''
def switch(data):
    
    def function_switch(x):
        print("Switch, " + data.__name__ + " returns:")
        data(x)
    return function_switch

def router(data):
    def function_wrapper(x):
        print("Router, " + data.__name__ + " returns:")
        print(x)
        return data(x)
    return function_wrapper
    
    
list=['192.168.17.1','up']
@router
def call(x):
   print(x)

call(list)
    