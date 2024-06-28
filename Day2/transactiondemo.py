# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:46:27 2018

@author: Balasubramaniam
"""

from customerdemo import Customer
from Ecommerce.test import check
from Ecommerce.product.productaccess import checkstock
import datetime
class Transaction:
    def __init__(self):
        self.__customer=""
        self.__tranId=0
        self.__tranDate=""
        self.__amount=0
        
    def setCustomer(self,customer):
        self.__customer=customer
        
    def getCustomer(self):
        return self.__customer
        
    def setTranId(self,id):
        self.__tranId=id
        
    def getTranId(self):
        return self.__tranId
    
    def setTranDate(self,tdate):
        self.__tranDate=tdate
        
    def getTranDate(self):
        return self.__tranDate
    
    def setAmount(self,amount):
        self.__amount=amount
        
    def getAmount(self):
        return self.__amount
    
print(check())    
print(checkstock())






