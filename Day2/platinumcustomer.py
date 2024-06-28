# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:02:21 2018

@author: Balasubramaniam
"""

from customerdemo import Customer
from transactiondemo import Transaction
class PlatinumCustomer(Customer,Transaction):
    def __init__(self,id,name,dob,discount,offer):
        self.__discount=discount
        self.__offer=offer
        Customer.__init__(self,id,name,dob)
        Transaction.__init__(self)

import datetime        
obj=PlatinumCustomer(2686,"Suman",datetime.date(1970,2,2),0.2,1000)
print(obj.getName())
          