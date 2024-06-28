# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:40:34 2018

@author: Balasubramaniam
"""

customers=[
        [4385687,"Prabhu","Chennai",True,[9952032862,99789678]],
         [43856856,"Suman","Bangalore",True,[9952032896]]
         ]
#print(type(customer))

print(customers[0][0])

org=["HCL","IBM"]
loc=["Chennai","Bangalore"]
for(x,y) in zip(org,loc):
    print(x,y)




  
