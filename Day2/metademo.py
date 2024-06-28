# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:28:48 2018

@author: Balasubramaniam
"""

class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)
    

class S:
    pass
class A(S, metaclass=LittleMeta):
    pass
a = A()








