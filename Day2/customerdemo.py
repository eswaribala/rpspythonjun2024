# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:25:32 2018

@author: Balasubramaniam
"""
#public without underscore
#protected with single underscore
#private with double underscore
class Customer:
    def __init__(self,id,name,dob):
        self.__id=id
        self.__name=name
        self.__dob=dob
        
    #setter method
    def setId(self,id):
        self.__id=id
    
    #getter method      
    def getId(self):
        return self.__id
        
    #setter method
    def setName(self,name):
        self.__name=name
    
    #getter method      
    def getName(self):
        return self.__name

#setter method
    def setDOB(self,dob):
        self.__dob=dob
    
    #getter method      
    def getDOB(self):
        return self.__dob   
        
        



