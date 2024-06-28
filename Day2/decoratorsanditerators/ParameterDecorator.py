'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

@morning_greeting
def call(x):
    print(x)

call("Hi")