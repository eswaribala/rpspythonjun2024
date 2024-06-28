# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:16:53 2018

@author: Balasubramaniam
"""
#conditional statements
import random

guess = random.randint(1000,10000)

if (guess>8000):
   print("Random number is higher than 5000")
elif ((guess>3000) and (guess<5000)):
     print("Random number is  between 3000 and 5000")
else:
    print("Random number is below 3000")
 
