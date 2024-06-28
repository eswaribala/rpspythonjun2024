# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:09:46 2018

@author: Balasubramaniam
"""

class Logging_Meta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        print(str.format("Allocating memory space for class {0} ", cls))
        return super().__new__(cls, name, bases, attrs, **kwargs)
    def __init__(self, name, bases, attrs, **kwargs):
        print(str.format("Initializing object {0}", self))
        return super().__init__(name, bases, attrs)
class LogClass(metaclass=Logging_Meta):
      def test(self):
        print("hello")
log_instance = LogClass()
log_instance.test()
print(log_instance)
print(type(LogClass))