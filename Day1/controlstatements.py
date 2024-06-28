# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:33:26 2018

@author: Balasubramaniam
"""

import random
#initial value, final value, step
for arg in range(1,10,2):
    value=random.randint(100,200)
    if value>150:
        print("Range is high")
    else:
        print("Range is low")